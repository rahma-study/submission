import pandas as pd
import streamlit as st
from pathlib import Path

# =========================
# KONFIGURASI DASHBOARD
# =========================
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)

PRIMARY_COLOR = "#23856D"
SECONDARY_COLOR = "#DCEFE8"

# =========================
# LOAD DATA
# =========================
BASE_DIR = Path(__file__).resolve().parent


@st.cache_data
def load_data():
    hour_path = BASE_DIR / "hour_clean.csv"
    day_path = BASE_DIR / "day_clean.csv"

    if not hour_path.exists():
        raise FileNotFoundError(
            f"File tidak ditemukan: {hour_path}"
        )

    if not day_path.exists():
        raise FileNotFoundError(
            f"File tidak ditemukan: {day_path}"
        )

    hourly = pd.read_csv(hour_path)
    daily = pd.read_csv(day_path)

    hourly["dteday"] = pd.to_datetime(hourly["dteday"])
    daily["dteday"] = pd.to_datetime(daily["dteday"])

    return hourly, daily


try:
    hour_df, day_df = load_data()
except Exception as e:
    st.error("Data dashboard gagal dimuat.")
    st.exception(e)
    st.stop()

# =========================
# LABEL KATEGORI
# =========================
season_labels = {
    1: "Musim semi",
    2: "Musim panas",
    3: "Musim gugur",
    4: "Musim dingin"
}

weather_labels = {
    1: "Cerah",
    2: "Berawan",
    3: "Hujan ringan",
    4: "Cuaca ekstrem"
}

# =========================
# SIDEBAR DAN FILTER
# =========================
with st.sidebar:
    st.markdown(
        f"""
        <div style="text-align:center; padding:12px 0 18px;">
            <div style="
                background-color:{SECONDARY_COLOR};
                border-radius:18px;
                width:90px;
                height:90px;
                margin:auto;
                display:flex;
                align-items:center;
                justify-content:center;
                font-size:48px;">
                🚲
            </div>
            <h2 style="margin-bottom:0; color:{PRIMARY_COLOR};">
                Pedal Insights
            </h2>
            <p style="font-size:13px; color:gray;">
                Bike Sharing Analytics
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()
    st.subheader("Filter Data")

    min_date = hour_df["dteday"].min().date()
    max_date = hour_df["dteday"].max().date()

    selected_dates = st.date_input(
        "Rentang Waktu",
        min_value=min_date,
        max_value=max_date,
        value=(min_date, max_date)
    )

    st.caption(
        "Pilih periode untuk memperbarui hasil analisis."
    )

# =========================
# MENANGANI RENTANG TANGGAL
# =========================
if isinstance(selected_dates, (tuple, list)):
    if len(selected_dates) == 2:
        start_date, end_date = selected_dates
    elif len(selected_dates) == 1:
        start_date = end_date = selected_dates[0]
    else:
        start_date, end_date = min_date, max_date
else:
    start_date = end_date = selected_dates

# =========================
# FILTER DATA PER JAM DAN PER HARI
# =========================
hour_filtered = hour_df[
    (hour_df["dteday"].dt.date >= start_date)
    & (hour_df["dteday"].dt.date <= end_date)
].copy()

day_filtered = day_df[
    (day_df["dteday"].dt.date >= start_date)
    & (day_df["dteday"].dt.date <= end_date)
].copy()

# =========================
# JUDUL DASHBOARD
# =========================
st.title("🚲 Bike Sharing Dashboard")

st.write(
    "Dashboard analisis pola penyewaan sepeda berdasarkan "
    "jam, musim, dan tren bulanan pada periode 2011–2012."
)

st.caption(
    f"Periode analisis: {start_date.strftime('%d %b %Y')} "
    f"- {end_date.strftime('%d %b %Y')}"
)

st.divider()

if hour_filtered.empty or day_filtered.empty:
    st.warning(
        "Data tidak tersedia untuk rentang tanggal yang dipilih."
    )
    st.stop()

# =========================
# PERHITUNGAN RINGKASAN
# =========================
hourly_avg = (
    hour_filtered.groupby("hr", as_index=False)["cnt"]
    .mean()
    .rename(columns={"cnt": "avg_rentals"})
)

peak_row = hourly_avg.loc[
    hourly_avg["avg_rentals"].idxmax()
]
peak_hour = int(peak_row["hr"])
peak_rentals = peak_row["avg_rentals"]

season_avg = (
    day_filtered.groupby("season", as_index=False)["cnt"]
    .mean()
    .rename(columns={"cnt": "avg_daily_rentals"})
)

season_avg["Musim"] = season_avg["season"].map(
    season_labels
)

best_season = season_avg.loc[
    season_avg["avg_daily_rentals"].idxmax()
]

worst_season = season_avg.loc[
    season_avg["avg_daily_rentals"].idxmin()
]

# =========================
# PERHITUNGAN TREN BULANAN
# =========================
monthly_avg = (
    day_filtered.assign(
        Tahun=day_filtered["dteday"].dt.year,
        Bulan=day_filtered["dteday"].dt.month
    )
    .groupby(["Tahun", "Bulan"], as_index=False)["cnt"]
    .mean()
    .rename(columns={"cnt": "Rata-rata Penyewaan Harian"})
)

monthly_avg["Periode"] = pd.to_datetime(
    monthly_avg["Tahun"].astype(str)
    + "-"
    + monthly_avg["Bulan"].astype(str)
    + "-01"
)

monthly_avg = monthly_avg.sort_values("Periode")

# =========================
# RINGKASAN PENYEWAAN
# =========================
st.subheader("Ringkasan Penyewaan")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Penyewaan",
        f"{hour_filtered['cnt'].sum():,.0f}"
    )

with col2:
    st.metric(
        "Jam Puncak Penyewaan",
        f"{peak_hour:02d}:00",
        f"{peak_rentals:,.2f} penyewaan/jam"
    )

with col3:
    st.metric(
        "Musim dengan Rata-rata Tertinggi",
        best_season["Musim"],
        f"{best_season['avg_daily_rentals']:,.2f} penyewaan/hari"
    )

st.divider()

# =========================
# VISUALISASI 1: PENYEWAAN PER JAM
# =========================
st.subheader(
    "1. Rata-rata Penyewaan Sepeda Berdasarkan Jam"
)

st.write(
    "Pola rata-rata penyewaan sepeda pada setiap jam "
    "dalam sehari."
)

hourly_chart = hourly_avg.rename(
    columns={
        "hr": "Jam",
        "avg_rentals": "Rata-rata Penyewaan"
    }
).copy()

hourly_chart["Jam"] = hourly_chart["Jam"].map(
    lambda h: f"{int(h):02d}:00"
)

st.line_chart(
    hourly_chart,
    x="Jam",
    y="Rata-rata Penyewaan",
    x_label="Jam dalam sehari",
    y_label="Rata-rata penyewaan per jam",
    color=PRIMARY_COLOR,
    height=380
)

st.info(
    f"Rata-rata penyewaan tertinggi terjadi pada pukul "
    f"{peak_hour:02d}:00, yaitu {peak_rentals:,.2f} "
    f"penyewaan per jam."
)

st.markdown(
    "**Rekomendasi operasional:** Pastikan ketersediaan "
    "sepeda mencukupi pada jam dengan permintaan tertinggi. "
    "Jadwalkan perawatan rutin pada jam yang rata-rata "
    "penyewaannya lebih rendah agar gangguan operasional "
    "dapat diminimalkan."
)

st.divider()

# =========================
# VISUALISASI 2: PENYEWAAN PER MUSIM
# =========================
st.subheader(
    "2. Rata-rata Penyewaan Harian Berdasarkan Musim"
)

st.write(
    "Perbandingan rata-rata jumlah penyewaan sepeda per hari "
    "pada setiap musim."
)

season_order = [
    "Musim semi",
    "Musim panas",
    "Musim gugur",
    "Musim dingin"
]

season_chart = (
    season_avg[["Musim", "avg_daily_rentals"]]
    .rename(
        columns={
            "avg_daily_rentals":
                "Rata-rata Penyewaan Harian"
        }
    )
    .set_index("Musim")
    .reindex(season_order)
    .dropna()
)

st.bar_chart(
    season_chart,
    color=PRIMARY_COLOR,
    height=350,
    y_label="Rata-rata penyewaan per hari"
)

col4, col5 = st.columns(2)

with col4:
    st.metric(
        "Rata-rata Tertinggi",
        best_season["Musim"],
        f"{best_season['avg_daily_rentals']:,.2f} penyewaan/hari"
    )

with col5:
    st.metric(
        "Rata-rata Terendah",
        worst_season["Musim"],
        f"{worst_season['avg_daily_rentals']:,.2f} penyewaan/hari"
    )

st.markdown(
    f"Rata-rata penyewaan harian tertinggi terjadi pada "
    f"**{best_season['Musim'].lower()}**, sebesar "
    f"{best_season['avg_daily_rentals']:,.2f} penyewaan per hari. "
    f"Rata-rata terendah terjadi pada "
    f"**{worst_season['Musim'].lower()}**, sebesar "
    f"{worst_season['avg_daily_rentals']:,.2f} penyewaan per hari."
)

st.markdown(
    "**Rekomendasi operasional:** Pertimbangkan penyesuaian "
    "ketersediaan armada berdasarkan rata-rata permintaan "
    "setiap musim. Promosi dapat diuji pada musim dengan "
    "permintaan lebih rendah, kemudian dievaluasi berdasarkan "
    "perubahan jumlah penyewaan."
)

# =========================
# TABEL RINCIAN MUSIM
# =========================
with st.expander("Lihat rincian rata-rata penyewaan per musim"):
    season_table = season_avg[
        ["Musim", "avg_daily_rentals"]
    ].rename(
        columns={
            "avg_daily_rentals":
                "Rata-rata Penyewaan per Hari"
        }
    )

    season_table["Rata-rata Penyewaan per Hari"] = (
        season_table["Rata-rata Penyewaan per Hari"].round(2)
    )

    st.dataframe(
        season_table,
        use_container_width=True,
        hide_index=True
    )

st.divider()

# =========================
# VISUALISASI 3: TREN BULANAN
# =========================
st.subheader(
    "3. Tren Rata-rata Penyewaan Sepeda per Bulan"
)

st.write(
    "Grafik ini menunjukkan perubahan rata-rata penyewaan "
    "sepeda harian dari bulan ke bulan selama periode analisis."
)

monthly_chart = monthly_avg.set_index("Periode")[
    ["Rata-rata Penyewaan Harian"]
]

st.line_chart(
    monthly_chart,
    color=PRIMARY_COLOR,
    height=350,
    y_label="Rata-rata penyewaan per hari"
)

if not monthly_avg.empty:
    highest_month = monthly_avg.loc[
        monthly_avg["Rata-rata Penyewaan Harian"].idxmax()
    ]

    lowest_month = monthly_avg.loc[
        monthly_avg["Rata-rata Penyewaan Harian"].idxmin()
    ]

    col_month1, col_month2 = st.columns(2)

    with col_month1:
        st.metric(
            "Rata-rata Tertinggi per Bulan",
            f"{highest_month['Rata-rata Penyewaan Harian']:,.2f}",
            f"{int(highest_month['Bulan']):02d}/{int(highest_month['Tahun'])}"
        )

    with col_month2:
        st.metric(
            "Rata-rata Terendah per Bulan",
            f"{lowest_month['Rata-rata Penyewaan Harian']:,.2f}",
            f"{int(lowest_month['Bulan']):02d}/{int(lowest_month['Tahun'])}"
        )

st.caption(
    "Rata-rata dihitung dari jumlah penyewaan harian "
    "pada setiap bulan dan tahun yang dipilih."
)

st.divider()

# =========================
# ANALISIS TAMBAHAN: CUACA
# =========================
with st.expander(
    "Analisis tambahan: Penyewaan berdasarkan cuaca"
):
    weather_avg = (
        hour_filtered.groupby("weathersit", as_index=False)["cnt"]
        .mean()
        .rename(columns={"cnt": "avg_rentals"})
    )

    weather_avg["Kondisi Cuaca"] = (
        weather_avg["weathersit"].map(weather_labels)
    )

    weather_chart = (
        weather_avg[["Kondisi Cuaca", "avg_rentals"]]
        .rename(
            columns={
                "avg_rentals": "Rata-rata Penyewaan"
            }
        )
        .set_index("Kondisi Cuaca")
        .sort_values("Rata-rata Penyewaan")
    )

    st.bar_chart(
        weather_chart,
        color=PRIMARY_COLOR,
        height=320,
        y_label="Rata-rata penyewaan per jam"
    )

# =========================
# TABEL DATA PENYEWAAN
# =========================
st.subheader("Data Penyewaan Sepeda")

with st.expander("Lihat data penyewaan per jam"):
    display_df = hour_filtered[
        [
            "dteday",
            "hr",
            "season",
            "weathersit",
            "casual",
            "registered",
            "cnt"
        ]
    ].copy()

    display_df["season"] = display_df["season"].map(
        season_labels
    )
    display_df["weathersit"] = display_df["weathersit"].map(
        weather_labels
    )

    display_df.columns = [
        "Tanggal",
        "Jam",
        "Musim",
        "Kondisi Cuaca",
        "Penyewa Kasual",
        "Penyewa Terdaftar",
        "Total Penyewaan"
    ]

    display_df["Tanggal"] = display_df["Tanggal"].dt.strftime(
        "%Y-%m-%d"
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

st.caption(
    "Sumber: Bike Sharing Dataset, Capital Bikeshare, 2011–2012."
)
