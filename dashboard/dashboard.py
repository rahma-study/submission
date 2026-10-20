
from pathlib import Path

import pandas as pd
import streamlit as st

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide",
)

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"


# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    file_path = DATA_DIR / "hour.csv"

    if not file_path.exists():
        raise FileNotFoundError(
            f"File dataset tidak ditemukan: {file_path}"
        )

    df = pd.read_csv(file_path)

    df["dteday"] = pd.to_datetime(df["dteday"], errors="coerce")

    # Nama hari untuk tampilan grafik
    day_names = {
        0: "Minggu",
        1: "Senin",
        2: "Selasa",
        3: "Rabu",
        4: "Kamis",
        5: "Jumat",
        6: "Sabtu",
    }

    if "weekday" in df.columns:
        df["nama_hari"] = df["weekday"].map(day_names)

    return df


try:
    df = load_data()
except Exception as error:
    st.error(f"Gagal memuat dataset: {error}")
    st.stop()


# =========================
# SIDEBAR FILTER
# =========================
st.sidebar.title("🔎 Filter Data")

min_date = df["dteday"].min().date()
max_date = df["dteday"].max().date()

date_range = st.sidebar.date_input(
    "Rentang tanggal",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)

if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date = date_range[0] if isinstance(date_range, (tuple, list)) else date_range
    end_date = start_date

available_hours = sorted(df["hr"].dropna().unique().astype(int))

selected_hours = st.sidebar.slider(
    "Rentang jam",
    min_value=int(min(available_hours)),
    max_value=int(max(available_hours)),
    value=(int(min(available_hours)), int(max(available_hours))),
)

# =========================
# FILTER DATA
# =========================
filtered_df = df[
    (df["dteday"].dt.date >= start_date)
    & (df["dteday"].dt.date <= end_date)
    & (df["hr"] >= selected_hours[0])
    & (df["hr"] <= selected_hours[1])
].copy()

# =========================
# JUDUL DASHBOARD
# =========================
st.title("🚲 Bike Sharing Dashboard")
st.markdown(
    "Dashboard interaktif untuk menganalisis pola penggunaan "
    "layanan penyewaan sepeda berdasarkan waktu."
)

st.divider()

if filtered_df.empty:
    st.warning("Tidak ada data untuk filter yang dipilih.")
    st.stop()

# =========================
# METRIK UTAMA
# =========================
total_rentals = int(filtered_df["cnt"].sum())
average_rentals = filtered_df["cnt"].mean()
registered_total = int(filtered_df["registered"].sum())
casual_total = int(filtered_df["casual"].sum())

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Penyewaan", f"{total_rentals:,}")
col2.metric("Rata-rata per Jam", f"{average_rentals:,.1f}")
col3.metric("Penyewa Terdaftar", f"{registered_total:,}")
col4.metric("Penyewa Kasual", f"{casual_total:,}")

st.divider()

# =========================
# GRAFIK 1: PENYEWAAN PER JAM
# =========================
st.subheader("📈 Tren Penyewaan Sepeda per Jam")

hourly_data = (
    filtered_df.groupby("hr", as_index=False)["cnt"]
    .mean()
    .sort_values("hr")
    .set_index("hr")
)

hourly_data.index.name = "Jam"
hourly_data = hourly_data.rename(
    columns={"cnt": "Rata-rata Penyewaan"}
)

st.line_chart(hourly_data, width="stretch")

# =========================
# GRAFIK 2: PENYEWAAN PER HARI
# =========================
st.subheader("📊 Rata-rata Penyewaan berdasarkan Hari")

if "nama_hari" in filtered_df.columns:
    weekday_data = (
        filtered_df.groupby("nama_hari")["cnt"]
        .mean()
        .reindex(
            ["Minggu", "Senin", "Selasa", "Rabu",
             "Kamis", "Jumat", "Sabtu"]
        )
        .dropna()
    )

    weekday_chart = weekday_data.to_frame(
        name="Rata-rata Penyewaan"
    )

    st.bar_chart(weekday_chart, width="stretch")
else:
    st.info("Kolom weekday tidak tersedia pada dataset.")

# =========================
# GRAFIK 3: PENYEWAAN PER BULAN
# =========================
st.subheader("📅 Total Penyewaan berdasarkan Bulan")

if "mnth" in filtered_df.columns:
    monthly_data = (
        filtered_df.groupby("mnth", as_index=False)["cnt"]
        .sum()
        .sort_values("mnth")
        .set_index("mnth")
    )

    monthly_data.index.name = "Bulan"
    monthly_data = monthly_data.rename(
        columns={"cnt": "Total Penyewaan"}
    )

    st.bar_chart(monthly_data, width="stretch")
else:
    st.info("Kolom mnth tidak tersedia pada dataset.")

# =========================
# TABEL DATA
# =========================
st.divider()
st.subheader("📋 Data Penyewaan Sepeda")

show_data = st.checkbox("Tampilkan data hasil filter", value=True)

if show_data:
    preferred_columns = [
        "dteday",
        "hr",
        "nama_hari",
        "casual",
        "registered",
        "cnt",
    ]

    display_columns = [
        column for column in preferred_columns
        if column in filtered_df.columns
    ]

    st.dataframe(
        filtered_df[display_columns],
        width="stretch",
        hide_index=True,
    )

    st.caption(
        f"Menampilkan {len(filtered_df):,} baris data."
    )

    csv_data = filtered_df[display_columns].to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇️ Download data CSV",
        data=csv_data,
        file_name="bike_sharing_filtered.csv",
        mime="text/csv",
        key="download_filtered_data",
    )
