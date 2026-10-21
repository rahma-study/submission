# 🚲 Pedal Insights: Bike Sharing Data Analysis

## Deskripsi Proyek

Pedal Insights merupakan proyek analisis data penyewaan sepeda menggunakan *Bike Sharing Dataset* tahun 2011–2012. Analisis ini bertujuan mengidentifikasi jam dengan rata-rata penyewaan tertinggi serta musim dengan rata-rata penyewaan harian tertinggi dan terendah untuk mendukung perencanaan operasional layanan sepeda.

Hasil analisis disajikan melalui notebook dan dashboard interaktif menggunakan Streamlit agar pola penyewaan sepeda berdasarkan waktu dan musim dapat dipahami dengan lebih mudah.

## Business Questions

Analisis ini berfokus pada dua pertanyaan bisnis utama:

1. Pada jam berapa rata-rata penyewaan sepeda per jam mencapai puncaknya selama periode 2011–2012, sehingga ketersediaan sepeda dan jadwal perawatan dapat disesuaikan untuk memenuhi permintaan pada jam sibuk tanpa mengganggu operasional?

2. Musim apa yang memiliki rata-rata penyewaan sepeda harian tertinggi dan terendah selama periode 2011–2012, sehingga jumlah armada dan strategi promosi dapat disesuaikan berdasarkan tingkat permintaan pada setiap musim?

## Dataset

Dataset yang digunakan adalah *Bike Sharing Dataset*, yang terdiri dari:

- `hour.csv`: data penyewaan sepeda per jam.
- `day.csv`: data penyewaan sepeda per hari.

Tahapan analisis meliputi pemeriksaan kualitas data, pembersihan data, eksplorasi data, visualisasi, analisis pola penyewaan, serta penyusunan kesimpulan dan rekomendasi.

## Hasil Analisis

Berdasarkan hasil eksplorasi data selama periode 2011–2012, diperoleh temuan berikut:

- **Jam dengan rata-rata penyewaan tertinggi:** pukul 17.00, dengan rata-rata sekitar 461,45 penyewaan sepeda per jam.
- **Musim dengan rata-rata penyewaan harian tertinggi:** musim gugur (*Fall*, season 3), dengan rata-rata sekitar 5.644,30 penyewaan sepeda per hari.
- **Musim dengan rata-rata penyewaan harian terendah:** musim semi (*Spring*, season 1), dengan rata-rata sekitar 2.604,13 penyewaan sepeda per hari.
- **Pola penyewaan berdasarkan jam:** rata-rata penyewaan cenderung lebih tinggi pada sore hari dan lebih rendah pada dini hari.

Temuan tersebut dapat digunakan sebagai pertimbangan dalam menentukan waktu penyediaan sepeda dan merencanakan operasional berdasarkan pola permintaan.

## Kesimpulan dan Rekomendasi

Analisis menunjukkan bahwa rata-rata penyewaan sepeda per jam mencapai nilai tertinggi pada pukul 17.00. Sementara itu, musim gugur (*Fall*, season 3) memiliki rata-rata penyewaan harian tertinggi, sedangkan musim semi (*Spring*, season 1) memiliki rata-rata terendah.

Berdasarkan hasil tersebut, pengelola layanan sepeda disarankan untuk:

- Memastikan ketersediaan sepeda mencukupi pada jam-jam dengan permintaan tinggi.
- Menjadwalkan perawatan rutin pada jam dengan rata-rata penyewaan lebih rendah agar gangguan operasional dapat diminimalkan.
- Menyesuaikan ketersediaan armada berdasarkan pola permintaan pada setiap musim.
- Mempertimbangkan promosi pada musim dengan permintaan lebih rendah dan mengevaluasi efektivitasnya berdasarkan perubahan jumlah penyewaan.

## Setup Environment

### Shell/Terminal

1. Unduh atau ekstrak proyek, kemudian buka folder utama proyek melalui terminal.
2. Buat dan aktifkan virtual environment sesuai sistem operasi yang digunakan.

**Windows (Command Prompt):**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Perbarui pip dan instal seluruh dependencies yang diperlukan.

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Pastikan file `requirements.txt` tersedia di folder utama proyek dan berisi seluruh library yang diperlukan.

## Instalasi dan Cara Menjalankan Dashboard

Pastikan virtual environment sudah aktif dan dependencies telah terinstal. Jalankan perintah berikut dari folder utama proyek:

```bash
streamlit run dashboard/dashboard.py
```

Dashboard akan terbuka melalui browser. Jika tidak terbuka secara otomatis, akses alamat lokal yang ditampilkan pada terminal.

## Teknologi yang Digunakan

- **Python** — bahasa pemrograman untuk analisis data.
- **Pandas** — untuk membaca dan mengolah dataset.
- **NumPy** — untuk mendukung operasi numerik.
- **Matplotlib dan Seaborn** — untuk membuat visualisasi pada notebook.
- **Streamlit** — untuk membangun dashboard interaktif.

## Dashboard

Dashboard Pedal Insights menyajikan ringkasan dan visualisasi data penyewaan sepeda berdasarkan jam, musim, tren bulanan, dan kondisi cuaca. Dashboard dilengkapi filter rentang tanggal yang memungkinkan pengguna mengeksplorasi pola penyewaan pada periode tertentu.

Jika dashboard telah di-deploy, tautan akses dapat dicantumkan pada file `url.txt`.
