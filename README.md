# 🚲 Pedal Insights: Bike Sharing Data Analysis

## Deskripsi Proyek

Pedal Insights merupakan proyek analisis data penyewaan sepeda menggunakan _Bike Sharing Dataset_ tahun 2011–2012. Analisis ini bertujuan mengidentifikasi jam dengan rata-rata penyewaan tertinggi serta musim dengan rata-rata penyewaan harian tertinggi dan terendah untuk mendukung perencanaan operasional layanan sepeda.

Hasil analisis disajikan melalui notebook dan dashboard interaktif menggunakan Streamlit agar pola penyewaan sepeda berdasarkan waktu dan musim dapat dipahami dengan lebih mudah.

## Business Questions

Analisis ini berfokus pada dua pertanyaan bisnis utama:

1. Pada jam berapa rata-rata penyewaan sepeda per jam mencapai puncaknya selama periode 2011–2012, sehingga ketersediaan sepeda dan jadwal perawatan dapat disesuaikan untuk memenuhi permintaan pada jam sibuk tanpa mengganggu operasional?

2. Musim apa yang memiliki rata-rata penyewaan sepeda harian tertinggi dan terendah selama periode 2011–2012, sehingga jumlah armada dan strategi promosi dapat disesuaikan berdasarkan tingkat permintaan pada setiap musim?

## Dataset

Dataset yang digunakan adalah _Bike Sharing Dataset_, yang terdiri dari:

- `hour.csv`: data penyewaan sepeda per jam.
- `day.csv`: data penyewaan sepeda per hari.

Tahapan analisis meliputi pengumpulan data, pemeriksaan kualitas data, pembersihan data, eksplorasi data, visualisasi, analisis pola penyewaan, serta penyusunan kesimpulan dan rekomendasi.

## Hasil Analisis

Berdasarkan hasil eksplorasi data selama periode 2011–2012, diperoleh temuan berikut:

- **Jam dengan rata-rata penyewaan tertinggi:** pukul 17.00, dengan rata-rata sekitar 461,45 penyewaan sepeda per jam.
- **Musim dengan rata-rata penyewaan harian tertinggi:** musim gugur (_Fall_, season 3), dengan rata-rata sekitar 5.644,30 penyewaan sepeda per hari.
- **Pola penyewaan berdasarkan jam:** rata-rata penyewaan cenderung lebih tinggi pada sore hari dan lebih rendah pada dini hari.

Temuan tersebut dapat digunakan sebagai pertimbangan dalam menentukan waktu penyediaan sepeda dan merencanakan operasional berdasarkan pola permintaan.

## Kesimpulan dan Rekomendasi

Analisis menunjukkan bahwa rata-rata penyewaan sepeda per jam mencapai nilai tertinggi pada pukul 17.00. Sementara itu, musim gugur (_Fall_, season 3) memiliki rata-rata penyewaan harian tertinggi dibandingkan musim lainnya.

Berdasarkan hasil tersebut, pengelola layanan sepeda disarankan untuk:

- Memastikan ketersediaan sepeda mencukupi pada jam-jam dengan permintaan tinggi.
- Menjadwalkan perawatan rutin pada jam dengan rata-rata penyewaan lebih rendah agar gangguan operasional dapat diminimalkan.
- Menyesuaikan ketersediaan armada berdasarkan pola permintaan pada setiap musim.
- Mempertimbangkan promosi pada musim dengan permintaan lebih rendah dan mengevaluasi efektivitasnya berdasarkan perubahan jumlah penyewaan.

## Instalasi dan Cara Menjalankan

Pastikan Python sudah terpasang di komputer.

1. Buka terminal pada folder utama proyek.
2. Instal library yang diperlukan:

   ```bash
   pip install -r requirements.txt
   ```

3. Jalankan dashboard:

   ```bash
   streamlit run dashboard/dashboard.py
   ```

4. Dashboard akan terbuka melalui browser. Jika tidak terbuka otomatis, akses alamat lokal yang ditampilkan di terminal.

## Teknologi yang Digunakan

- **Python** — bahasa pemrograman untuk analisis data.
- **Pandas** — untuk membaca dan mengolah dataset.
- **NumPy** — untuk mendukung operasi numerik.
- **Matplotlib dan Seaborn** — untuk membuat visualisasi pada notebook.
- **Streamlit** — untuk membangun dashboard interaktif.

## Dashboard

Dashboard Pedal Insights menyajikan ringkasan dan visualisasi data penyewaan sepeda berdasarkan jam, musim, dan kondisi cuaca. Dashboard dilengkapi filter rentang tanggal yang memungkinkan pengguna mengeksplorasi pola penyewaan pada periode tertentu.

Jika dashboard telah di-deploy, tautan akses dapat dicantumkan pada file `url.txt`.
