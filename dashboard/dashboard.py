import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
TEXT_COLOR = "#263A35"

sns.set_theme(style="whitegrid")

plt.rcParams.update({
    "font.family": "sans-serif",
    "axes.labelcolor": TEXT_COLOR,
    "xtick.color": TEXT_COLOR,
    "ytick.color": TEXT_COLOR,
    "text.color": TEXT_COLOR,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "axes.edgecolor": "#D9E2DE"
})

# =========================
# LOKASI DATA
# =========================
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"


# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    hour_path = DATA_DIR / "hour.csv"
    day_path = DATA_DIR / "day.csv"

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
# LABEL MUSIM DAN CUACA
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

season_order = [
    "Musim semi",
    "Musim panas",
    "Musim gugur",
    "Musim dingin"
]


# =========================
# SIDEBAR: LOGO DAN FILTER
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
        value=(min_date, max_date),
        format="DD/MM/YYYY"
    )

    st.caption("Pilih rentang tanggal untuk memperbarui analisis.")


# =========================
# MENANGANI PILIHAN TANGGAL
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
# FILTER DATA
# =========================
main_df = hour_df[
    (hour_df["dteday"].dt.date >= start_date)
    & (hour_df["dteday"].dt.date <= end_date)
].copy()


# =========================
# HEADER DASHBOARD
# =========================
st.title("🚲 Bike Sharing Dashboard")

st.write(
    "Dashboard untuk memahami pola penyewaan sepeda "
    "berdasarkan jam, musim, dan kondisi cuaca."
)

st.caption(
    f"Periode analisis: {start_date.strftime('%d %b %Y')} "
    f"- {end_date.strftime('%d %b %Y')}"
)

st.divider()

if main_df.empty:
    st.warning(
        "Tidak ada data pada rentang tanggal yang dipilih."
    )
    st.stop()


# =========================
# RINGKASAN PENYEWAAN
# =========================
st.subheader("Ringkasan Penyewaan")

total_rentals = main_df["cnt"].sum()
average_rentals = main_df["cnt"].mean()

hourly_avg = (
    main_df.groupby("hr", as_index=False)["cnt"]
    .mean()
)

peak_hour = int(
    hourly_avg.loc[hourly_avg["cnt"].idxmax(), "hr"]
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Total Penyewaan",
        value=f"{total_rentals:,.0f}"
    )

with col2:
    st.metric(
        label="Rata-rata Penyewaan per Jam",
        value=f"{average_rentals:,.1f}"
    )

with col3:
    st.metric(
        label="Jam dengan Rata-rata Tertinggi",
        value=f"{peak_hour:02d}:00"
    )

st.divider()


# =========================
# GRAFIK 1: POLA PER JAM
# =========================
st.subheader("Pola Penyewaan Berdasarkan Jam")

fig, ax = plt.subplots(figsize=(12, 4.5))

ax.plot(
    hourly_avg["hr"],
    hourly_avg["cnt"],
    color=PRIMARY_COLOR,
    linewidth=2.5,
    marker="o",
    markersize=5,
    markerfacecolor="white",
    markeredgewidth=1.8
)

ax.fill_between(
    hourly_avg["hr"],
    hourly_avg["cnt"],
    color=SECONDARY_COLOR,
    alpha=0.65
)

ax.set_xlabel("Jam", fontsize=11)
ax.set_ylabel("Rata-rata Penyewaan", fontsize=11)

ax.set_xticks(range(24))
ax.set_xticklabels(
    [f"{h:02d}:00" for h in range(24)],
    rotation=0,
    ha="center",
    fontsize=8
)

ax.grid(axis="y", alpha=0.25)
ax.grid(axis="x", visible=False)
ax.set_axisbelow(True)
ax.margins(x=0.02, y=0.15)

sns.despine(ax=ax)
fig.tight_layout()

st.pyplot(fig, use_container_width=True)
plt.close(fig)

st.caption(
    f"Puncak rata-rata penyewaan pada periode terpilih: "
    f"{peak_hour:02d}:00."
)

st.divider()


# =========================
# MENYIAPKAN DATA MUSIM
# =========================
season_avg = (
    main_df.groupby("season", as_index=False)["cnt"]
    .mean()
)

season_avg["Musim"] = (
    season_avg["season"].map(season_labels)
)

season_avg = season_avg.dropna(subset=["Musim"])


# =========================
# MENYIAPKAN DATA CUACA
# =========================
weather_avg = (
    main_df.groupby("weathersit", as_index=False)["cnt"]
    .mean()
)

weather_avg["Kondisi Cuaca"] = (
    weather_avg["weathersit"].map(weather_labels)
)

weather_avg = weather_avg.dropna(subset=["Kondisi Cuaca"])


# =========================
# GRAFIK 2 DAN 3
# =========================
col1, col2 = st.columns(2)

# =========================
# GRAFIK 2: MUSIM
# =========================
with col1:
    st.subheader("Penyewaan Berdasarkan Musim")

    season_chart = season_avg.copy()
    season_chart["Musim"] = pd.Categorical(
        season_chart["Musim"],
        categories=season_order,
        ordered=True
    )
    season_chart = season_chart.sort_values("Musim")

    fig, ax = plt.subplots(figsize=(7, 4.5))

    bars = sns.barplot(
        data=season_chart,
        x="Musim",
        y="cnt",
        color=PRIMARY_COLOR,
        ax=ax
    )

    ax.set_xlabel("")
    ax.set_ylabel("Rata-rata Penyewaan", fontsize=10)

    ax.tick_params(
        axis="x",
        labelrotation=0,
        labelsize=9
    )

    ax.grid(axis="y", alpha=0.25)
    ax.grid(axis="x", visible=False)
    ax.set_axisbelow(True)

    for container in ax.containers:
        ax.bar_label(
            container,
            fmt="%.1f",
            padding=3,
            fontsize=9
        )

    ax.margins(y=0.15)
    sns.despine(ax=ax)
    fig.tight_layout()

    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    if not season_avg.empty:
        best_season = season_avg.loc[
            season_avg["cnt"].idxmax()
        ]

        st.caption(
            f"Rata-rata tertinggi: {best_season['Musim']} "
            f"({best_season['cnt']:,.1f} penyewaan)."
        )


# =========================
# GRAFIK 3: CUACA
# =========================
with col2:
    st.subheader("Penyewaan Berdasarkan Cuaca")

    weather_chart = weather_avg.sort_values(
        "cnt",
        ascending=False
    ).copy()

    fig, ax = plt.subplots(figsize=(7, 4.5))

    sns.barplot(
        data=weather_chart,
        x="Kondisi Cuaca",
        y="cnt",
        color=PRIMARY_COLOR,
        ax=ax
    )

    ax.set_xlabel("")
    ax.set_ylabel("Rata-rata Penyewaan", fontsize=10)

    ax.tick_params(
        axis="x",
        labelrotation=0,
        labelsize=9
    )

    ax.grid(axis="y", alpha=0.25)
    ax.grid(axis="x", visible=False)
    ax.set_axisbelow(True)

    for container in ax.containers:
        ax.bar_label(
            container,
            fmt="%.1f",
            padding=3,
            fontsize=9
        )

    ax.margins(y=0.15)
    sns.despine(ax=ax)
    fig.tight_layout()

    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    if not weather_avg.empty:
        best_weather = weather_avg.loc[
            weather_avg["cnt"].idxmax()
        ]

        st.caption(
            f"Rata-rata tertinggi pada kondisi "
            f"{best_weather['Kondisi Cuaca']} "
            f"({best_weather['cnt']:,.1f} penyewaan)."
        )

st.divider()


# =========================
# TABEL DATA PENYEWAAN
# =========================
st.subheader("Data Penyewaan Sepeda")

with st.expander("Lihat data penyewaan"):
    display_df = main_df[
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

    display_df["season"] = (
        display_df["season"].map(season_labels)
    )

    display_df["weathersit"] = (
        display_df["weathersit"].map(weather_labels)
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

    display_df["Tanggal"] = (
        display_df["Tanggal"].dt.strftime("%Y-%m-%d")
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )


# =========================
# SUMBER DATA
# =========================
st.caption(
    "Sumber: Bike Sharing Dataset, "
    "Capital Bikeshare, 2011–2012."
)
