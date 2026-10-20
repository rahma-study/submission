# 🚲 Pedal Insights: Bike Sharing Data Analysis

## Deskripsi Proyek

Proyek ini bertujuan menganalisis pola penyewaan sepeda menggunakan _Bike Sharing Dataset_ tahun 2011–2012. Analisis dilakukan untuk memahami waktu dengan permintaan penyewaan tertinggi serta hubungan musim dan kondisi cuaca dengan jumlah penyewaan sepeda.

Hasil analisis disajikan dalam bentuk visualisasi interaktif menggunakan Streamlit agar pola penyewaan dapat dipahami dengan lebih mudah.

## Business Questions

Analisis ini berfokus pada dua pertanyaan utama:

1. Bagaimana rata-rata jumlah penyewaan sepeda berdasarkan jam, dan pada jam berapa permintaan mencapai puncaknya?
2. Bagaimana rata-rata jumlah penyewaan sepeda berdasarkan musim dan kondisi cuaca, serta kombinasi mana yang memiliki rata-rata penyewaan tertinggi?

## Dataset

Dataset yang digunakan adalah _Bike Sharing Dataset_, yang terdiri dari data penyewaan sepeda per jam (`hour.csv`) dan per hari (`day.csv`).

Tahapan analisis meliputi pengumpulan data, pemeriksaan kualitas data, pembersihan data, eksplorasi data, visualisasi, serta penyusunan kesimpulan dan rekomendasi.

## Hasil Analisis

Berdasarkan hasil eksplorasi data, diperoleh beberapa temuan utama:

- **Jam penyewaan tertinggi:** pukul 17.00, dengan rata-rata 461,45 penyewaan sepeda.
- **Musim dengan rata-rata penyewaan tertinggi:** musim gugur (_fall_), dengan rata-rata 236,02 penyewaan.
- **Kondisi cuaca:** cuaca cerah atau sedikit berawan memiliki rata-rata penyewaan tertinggi, yaitu 204,87.
- **Kombinasi musim dan cuaca:** musim gugur dengan cuaca cerah atau sedikit berawan memiliki rata-rata penyewaan tertinggi, yaitu 244,49.

Temuan ini menunjukkan bahwa waktu dan kondisi lingkungan perlu dipertimbangkan dalam perencanaan ketersediaan sepeda.

## Kesimpulan dan Rekomendasi

Penyewaan sepeda cenderung mencapai puncaknya pada sore hari, terutama pukul 17.00–18.00. Rata-rata penyewaan juga berbeda berdasarkan musim dan kondisi cuaca.

Berdasarkan temuan tersebut, pengelola layanan sepeda disarankan untuk menyesuaikan ketersediaan sepeda dengan jam permintaan tinggi serta mempertimbangkan pola musiman dan kondisi cuaca dalam perencanaan operasional.

## Instalasi dan Cara Menjalankan

Pastikan Python sudah terpasang di komputer.

1. Instal library yang diperlukan dengan menjalankan perintah berikut di terminal:

   ```bash
   pip install -r requirements.txt
   ```

2. Jalankan dashboard dari folder utama proyek:

   ```bash
   streamlit run dashboard/dashboard.py
   ```

3. Dashboard akan terbuka melalui browser. Jika tidak terbuka otomatis, ikuti alamat lokal yang ditampilkan di terminal.

## Teknologi yang Digunakan

- **Python** — bahasa pemrograman yang digunakan dalam proses analisis data.
- **Pandas** — digunakan untuk membaca, membersihkan, dan mengolah dataset.
- **NumPy** — mendukung operasi numerik dalam analisis data.
- **Matplotlib dan Seaborn** — digunakan untuk membuat visualisasi data pada notebook.
- **Streamlit** — digunakan untuk membangun dashboard interaktif yang menampilkan hasil analisis.

## Dashboard

Dashboard menampilkan ringkasan data penyewaan sepeda, visualisasi rata-rata penyewaan berdasarkan jam, serta analisis berdasarkan musim dan kondisi cuaca.

Jika dashboard telah di-deploy, tautan akses dapat dicantumkan di file `url.txt`.
