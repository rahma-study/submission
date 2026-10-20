```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from pathlib import Path

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Dashboard Bike Sharing",
    page_icon="🚲",
    layout="wide"
)

sns.set_theme(style="whitegrid")
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.facecolor"] = "white"

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
# JUDUL DASHBOARD
# =========================
st.title("🚲 Bike Sharing Dashboard")
st.write("Analisis penggunaan sepeda berdasarkan waktu, musim, dan kondisi cuaca.")

# =========================
# FILTER TANGGAL
# =========================
min_date = day_df["dteday"].min().date()
max_date = day_df["dteday"].max().date()

date_range = st.date_input(
    "Pilih rentang tanggal",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(date_range) == 2:
    start_date, end_date = date_range

    main_df = day_df[
        (day_df["dteday"].dt.date >= start_date) &
        (day_df["dteday"].dt.date <= end_date)
    ]

    hourly_df = hour_df[
        (hour_df["dteday"].dt.date >= start_date) &
        (hour_df["dteday"].dt.date <= end_date)
    ]
else:
    main_df = day_df.copy()
    hourly_df = hour_df.copy()

# =========================
# ANALISIS DATA
# =========================
if not main_df.empty:

    # METRIK
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Penyewaan",
        f"{main_df['cnt'].sum():,}"
    )

    col2.metric(
        "Rata-rata Penyewaan Harian",
        f"{main_df['cnt'].mean():,.0f}"
    )

    col3.metric(
        "Total Hari",
        len(main_df)
    )

    st.divider()

    # =========================
    # GRAFIK 1: PENYEWAAN PER JAM
    # =========================
    st.subheader("Pola Penyewaan Sepeda per Jam")

    if not hourly_df.empty:
        hourly_rentals = hourly_df.groupby("hr")["cnt"].mean()

        fig, ax = plt.subplots(figsize=(12, 5))

        ax.plot(
            hourly_rentals.index,
            hourly_rentals.values,
            marker="o",
            linewidth=2.5,
            markersize=6
        )

        ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Jam")
        ax.set_xlabel("Jam")
        ax.set_ylabel("Rata-rata Penyewaan")
        ax.set_xticks(range(24))
        ax.tick_params(axis="x", rotation=0)
        ax.grid(True, alpha=0.3)

        fig.tight_layout()
        st.pyplot(fig)
        plt.close(fig)
    else:
        st.info("Tidak ada data per jam pada rentang tanggal yang dipilih.")

    # =========================
    # GRAFIK 2: PENYEWAAN PER MUSIM
    # =========================
    st.subheader("Penyewaan Sepeda Berdasarkan Musim")

    season_names = {
        1: "Musim Semi",
        2: "Musim Panas",
        3: "Musim Gugur",
        4: "Musim Dingin"
    }

    season_df = main_df.copy()
    season_df["Musim"] = season_df["season"].map(season_names)

    season_rentals = (
        season_df.groupby("Musim", as_index=False)["cnt"]
        .mean()
    )

    season_order = [
        "Musim Semi",
        "Musim Panas",
        "Musim Gugur",
        "Musim Dingin"
    ]

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.barplot(
        data=season_rentals,
        x="Musim",
        y="cnt",
        order=season_order,
        ax=ax
    )

    ax.set_title("Rata-rata Penyewaan Sepeda per Musim")
    ax.set_xlabel("Musim")
    ax.set_ylabel("Rata-rata Penyewaan")
    ax.tick_params(axis="x", rotation=0)

    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    # =========================
    # GRAFIK 3: PENYEWAAN BERDASARKAN CUACA
    # =========================
    st.subheader("Penyewaan Sepeda Berdasarkan Kondisi Cuaca")

    weather_names = {
        1: "Cerah",
        2: "Berkabut",
        3: "Hujan Ringan",
        4: "Hujan Lebat"
    }

    weather_df = main_df.copy()
    weather_df["Cuaca"] = weather_df["weathersit"].map(weather_names)

    weather_rentals = (
        weather_df.groupby("Cuaca", as_index=False)["cnt"]
        .mean()
        .sort_values("cnt")
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    bars = ax.barh(
        weather_rentals["Cuaca"],
        weather_rentals["cnt"]
    )

    ax.set_title("Rata-rata Penyewaan Berdasarkan Cuaca")
    ax.set_xlabel("Rata-rata Penyewaan")
    ax.set_ylabel("Kondisi Cuaca")

    ax.bar_label(bars, fmt="%.0f", padding=4)
    fig.tight_layout()

    st.pyplot(fig)
    plt.close(fig)

    # =========================
    # TABEL DATA
    # =========================
    with st.expander("Lihat Data Penyewaan Harian"):
        st.dataframe(main_df, use_container_width=True)

else:
    st.warning("Tidak ada data untuk rentang tanggal yang dipilih.")
```
