# 🚲 Pedal Insights: Bike Sharing Data Analysis

## Deskripsi Proyek

Proyek ini bertujuan menganalisis pola penyewaan sepeda menggunakan *Bike Sharing Dataset* tahun 2011–2012. Analisis difokuskan pada identifikasi jam dengan rata-rata penyewaan tertinggi dan musim dengan rata-rata penyewaan harian tertinggi.

Hasil analisis disajikan melalui visualisasi data pada notebook dan dashboard interaktif menggunakan Streamlit agar pola penyewaan sepeda dapat dipahami dengan lebih mudah.

## Business Questions

Analisis ini berfokus pada dua pertanyaan bisnis utama:

1. Pada periode 2011–2012, pukul berapa rata-rata penyewaan sepeda per jam mencapai nilai tertinggi?
2. Pada periode 2011–2012, musim apa yang memiliki rata-rata penyewaan sepeda harian tertinggi?

## Dataset

Dataset yang digunakan adalah *Bike Sharing Dataset*, yang terdiri dari data penyewaan sepeda per jam (`hour.csv`) dan per hari (`day.csv`).

Tahapan analisis meliputi pengumpulan data, pemeriksaan kualitas data, pembersihan data, eksplorasi data, visualisasi, analisis lanjutan, serta penyusunan kesimpulan dan rekomendasi.

## Hasil Analisis

Berdasarkan hasil eksplorasi data, diperoleh beberapa temuan utama:

- **Jam dengan rata-rata penyewaan tertinggi:** pukul 17.00, dengan rata-rata sekitar 461,45 penyewaan sepeda per jam.
- **Musim dengan rata-rata penyewaan harian tertinggi:** season 3, dengan rata-rata sekitar 5.644,30 penyewaan sepeda per hari.
- **Pola permintaan berdasarkan jam:** rata-rata penyewaan cenderung lebih tinggi pada sore hari dan lebih rendah pada dini hari.

Temuan tersebut menunjukkan bahwa waktu penyewaan dan pola musiman dapat menjadi pertimbangan dalam perencanaan ketersediaan sepeda.

## Kesimpulan dan Rekomendasi

Analisis menunjukkan bahwa rata-rata penyewaan sepeda per jam mencapai nilai tertinggi pada pukul 17.00. Sementara itu, berdasarkan rata-rata penyewaan harian, season 3 memiliki nilai tertinggi dibandingkan musim lainnya.

Berdasarkan temuan tersebut, pengelola layanan sepeda disarankan untuk memperhatikan ketersediaan sepeda pada jam-jam dengan permintaan tinggi serta mempertimbangkan perbedaan pola penyewaan antar musim dalam perencanaan operasional.

## Instalasi dan Cara Menjalankan

Pastikan Python sudah terpasang di komputer.

1. Instal library yang diperlukan melalui terminal:

   ```bash
   pip install -r requirements.txt
   ```

2. Jalankan dashboard dari folder utama proyek:

   ```bash
   streamlit run dashboard/dashboard.py
   ```

3. Dashboard akan terbuka melalui browser. Jika tidak terbuka otomatis, akses alamat lokal yang ditampilkan di terminal.

## Teknologi yang Digunakan

- **Python** — bahasa pemrograman untuk proses analisis data.
- **Pandas** — untuk membaca, membersihkan, dan mengolah dataset.
- **NumPy** — untuk mendukung operasi numerik.
- **Matplotlib dan Seaborn** — untuk membuat visualisasi data pada notebook.
- **Streamlit** — untuk membangun dashboard interaktif.

## Dashboard

Dashboard menampilkan ringkasan data penyewaan sepeda dan visualisasi yang mendukung kedua pertanyaan bisnis, yaitu rata-rata penyewaan sepeda berdasarkan jam serta rata-rata penyewaan sepeda harian berdasarkan musim.

Jika dashboard telah di-deploy, tautan akses dapat dicantumkan di file `url.txt`.
