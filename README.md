# Pedal Insights 🚲

### Bike Sharing Data Analysis Dashboard

Pedal Insights adalah dashboard interaktif untuk mengeksplorasi pola penyewaan sepeda berdasarkan waktu, musim, dan kondisi cuaca menggunakan **Bike Sharing Dataset**. Dashboard dibangun dengan Python dan Streamlit untuk membantu pengguna memahami pola penggunaan sepeda melalui visualisasi yang mudah dibaca.

## Latar Belakang

Analisis ini berfokus pada pola jumlah penyewaan sepeda dan bagaimana pola tersebut berbeda menurut jam dalam sehari, musim, serta kondisi cuaca. Hasilnya ditampilkan melalui grafik interaktif agar tren utama lebih mudah diamati.

## Pertanyaan Analisis

1. Bagaimana pola rata-rata penyewaan sepeda berdasarkan jam dalam sehari?
2. Bagaimana pola rata-rata penyewaan sepeda berdasarkan musim dan kondisi cuaca?

## Ringkasan Temuan

Berdasarkan analisis yang telah dilakukan:

- Rata-rata penyewaan per jam tertinggi tercatat pada pukul **17.00** (sekitar **461,45**) dan pukul **18.00** (sekitar **425,51**).
- Rata-rata penyewaan terendah tercatat pada pukul **04.00** (sekitar **6,35**).
- Berdasarkan musim, **musim 3** memiliki rata-rata penyewaan sekitar **236,02**, sedangkan musim 1 sekitar **111,11**.
- Pada kategori cuaca, **cuaca 1** (cerah atau sedikit berawan) memiliki rata-rata penyewaan sekitar **204,87**.
- Kombinasi musim 3 dan cuaca 1 menunjukkan rata-rata penyewaan sekitar **244,49**.

> Catatan: nilai di atas adalah rata-rata berdasarkan analisis sebelumnya, bukan total penyewaan. Pastikan angka ini konsisten dengan notebook final sebelum submission.

## Struktur Proyek

```text
submission_bike_sharing/
├── dashboard/
│   └── dashboard.py
├── data/
│   ├── day.csv
│   └── hour.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

## Setup Environment

Pastikan Python telah terpasang. Buka terminal pada **folder utama** `submission_bike_sharing`, yaitu folder yang berisi `dashboard`, `data`, dan `requirements.txt`.

### Opsi 1 — Shell / Terminal

Buat virtual environment (opsional tetapi disarankan):

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install library yang diperlukan:

```bash
python -m pip install -r requirements.txt
```

### Opsi 2 — Anaconda

Jika menggunakan Anaconda, buat dan aktifkan environment:

```bash
conda create --name bike-sharing python=3.12
conda activate bike-sharing
python -m pip install -r requirements.txt
```

## ▶️ Menjalankan Dashboard

Jalankan perintah berikut dari **folder utama proyek**:

```bash
streamlit run dashboard/dashboard.py
```

Streamlit akan menampilkan alamat lokal di terminal. Buka alamat tersebut di browser untuk melihat dashboard.

Jika perintah tidak menemukan file, pastikan terminal berada di folder `submission_bike_sharing`, bukan di dalam folder `dashboard`.

## Dataset

Dashboard menggunakan file CSV berikut:

- `data/hour.csv` — data penyewaan sepeda per jam.
- `data/day.csv` — data penyewaan sepeda per hari.

Simpan file dataset di folder `data/` sesuai struktur proyek di atas.

## Teknologi yang Digunakan

- **Python** — bahasa pemrograman.
- **Pandas** — membaca dan mengolah data.
- **NumPy** — operasi numerik.
- **Matplotlib** — visualisasi data.
- **Seaborn** — visualisasi statistik (jika digunakan dalam kode analisis).
- **Streamlit** — membangun dashboard interaktif.

## Dashboard Online

URL dashboard Streamlit Community Cloud akan ditambahkan setelah deployment berhasil.

## Catatan Penggunaan

Pastikan `requirements.txt`, folder `data/`, dan file `dashboard/dashboard.py` sudah tersedia sebelum menjalankan aplikasi. Untuk hasil analisis yang dapat direproduksi, gunakan notebook dan dataset yang sama dengan yang digunakan dalam dashboard.
