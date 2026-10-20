import pandas as pd
import matplotlib
matplotlib.use("Agg")
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

sns.set_theme(style="whitegrid")

PRIMARY_COLOR = "#23856D"
SECONDARY_COLOR = "#DCEFE8"
TEXT_COLOR = "#263A35"

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
# LOAD DATA
# =========================
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"

hour_df = pd.read_csv(DATA_DIR / "hour.csv")
day_df = pd.read_csv(DATA_DIR / "day.csv")

hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])
day_df["dteday"] = pd.to_datetime(day_df["dteday"])

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

# =========================
# SIDEBAR: LOGO DAN FILTER
# =========================
with st.sidebar:
    st.markdown(
        f"""
        <div style="text-align:center; padding:12px 0 18px 0;">
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

    st.caption("Pilih periode untuk memperbarui analisis.")

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
st.title("Bike Sharing Dashboard")

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

else:
    # =========================
    # RINGKASAN PENYEWAAN
    # =========================
    st.subheader("Ringkasan Penyewaan")

    total_rentals = main_df["cnt"].sum()
    average_rentals = main_df["cnt"].mean()

    hourly_avg = (
        main_df.groupby("hr")["cnt"].mean()
    )
    peak_hour = int(hourly_avg.idxmax())

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

    hourly_avg = (
        main_df.groupby("hr", as_index=False)["cnt"]
        .mean()
    )

    fig, ax = plt.subplots(figsize=(12, 4.5))

    ax.plot(
        hourly_avg["hr"],
        hourly_avg["cnt"],
        color=PRIMARY_COLOR,
        linewidth=2.5,
        marker="o",
        markersize=4
    )

    ax.fill_between(
        hourly_avg["hr"],
        hourly_avg["cnt"],
        color=SECONDARY_COLOR,
        alpha=0.75
    )

    ax.set_xlabel("Jam")
    ax.set_ylabel("Rata-rata Penyewaan")
    ax.set_xticks(range(24))
    ax.set_xticklabels(
        [f"{hour:02d}:00" for hour in range(24)],
        rotation=45,
        ha="right",
        fontsize=9
    )

    ax.grid(axis="y", alpha=0.25)
    ax.grid(axis="x", visible=False)
    ax.margins(y=0.15)

    sns.despine(ax=ax)
    fig.tight_layout()

    st.pyplot(fig, width="stretch")
    plt.close(fig)

    st.divider()

    # =========================
    # GRAFIK 2: MUSIM
    # =========================
    col1, col2 = st.columns(2)

    season_avg = (
        main_df.groupby("season", as_index=False)["cnt"]
        .mean()
    )

    # Pastikan urutan musim tetap 1 sampai 4
    season_avg["Musim"] = (
        season_avg["season"].map(season_labels)
    )

    with col1:
        st.subheader("Penyewaan Berdasarkan Musim")

        fig, ax = plt.subplots(figsize=(6, 4.5))

        sns.barplot(
            data=season_avg,
            x="Musim",
            y="cnt",
            color=PRIMARY_COLOR,
            ax=ax
        )

        ax.set_xlabel("")
        ax.set_ylabel("Rata-rata Penyewaan")
        ax.tick_params(
            axis="x",
            rotation=0,
            labelsize=9
        )

        ax.grid(axis="y", alpha=0.25)
        ax.grid(axis="x", visible=False)
        ax.set_axisbelow(True)

        sns.despine(ax=ax)
        fig.tight_layout()

        st.pyplot(fig, width="stretch")
        plt.close(fig)

    # =========================
    # GRAFIK 3: KONDISI CUACA
    # =========================
    weather_avg = (
        main_df.groupby("weathersit", as_index=False)["cnt"]
        .mean()
    )

    weather_avg["Kondisi Cuaca"] = (
        weather_avg["weathersit"].map(weather_labels)
    )

    # Urutkan dari rata-rata terendah ke tertinggi
    weather_avg = weather_avg.sort_values(
        "cnt",
        ascending=True
    )

    with col2:
        st.subheader("Penyewaan Berdasarkan Cuaca")

        fig, ax = plt.subplots(figsize=(6, 4.5))

        sns.barplot(
            data=weather_avg,
            x="cnt",
            y="Kondisi Cuaca",
            color=PRIMARY_COLOR,
            ax=ax
        )

        ax.set_xlabel("Rata-rata Penyewaan")
        ax.set_ylabel("")
        ax.tick_params(
            axis="y",
            rotation=0,
            labelsize=9
        )

        ax.grid(axis="x", alpha=0.25)
        ax.grid(axis="y", visible=False)
        ax.set_axisbelow(True)

        # Tampilkan nilai di ujung setiap batang
        for container in ax.containers:
            ax.bar_label(
                container,
                fmt="%.0f",
                padding=4,
                fontsize=9
            )

        ax.margins(x=0.18)

        sns.despine(ax=ax)
        fig.tight_layout()

        st.pyplot(fig, width="stretch")
        plt.close(fig)

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

    st.caption(
        "Sumber: Bike Sharing Dataset, "
        "Capital Bikeshare, 2011–2012."
    )
