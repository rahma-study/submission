# 🚲 Pedal Insights: Bike Sharing Data Analysis

## Deskripsi Proyek

Pedal Insights merupakan proyek analisis data penyewaan sepeda menggunakan *Bike Sharing Dataset* tahun 2011–2012. Analisis ini berfokus pada identifikasi jam dengan rata-rata penyewaan tertinggi dan musim dengan rata-rata penyewaan harian tertinggi.

Hasil analisis disajikan melalui notebook dan dashboard interaktif menggunakan Streamlit untuk membantu memahami pola penyewaan sepeda berdasarkan waktu dan musim.

## Business Questions

Analisis ini berfokus pada dua pertanyaan bisnis utama:

1. Pada periode 2011–2012, pukul berapa rata-rata penyewaan sepeda per jam mencapai nilai tertinggi?
2. Pada periode 2011–2012, musim apa yang memiliki rata-rata penyewaan sepeda harian tertinggi?

## Dataset

Dataset yang digunakan adalah *Bike Sharing Dataset*, yang terdiri dari:

- `hour.csv`: data penyewaan sepeda per jam.
- `day.csv`: data penyewaan sepeda per hari.

Tahapan analisis meliputi pengumpulan data, pemeriksaan kualitas data, pembersihan data, eksplorasi data, visualisasi, serta penyusunan kesimpulan dan rekomendasi.

## Hasil Analisis

Berdasarkan hasil eksplorasi data periode 2011–2012, diperoleh temuan berikut:

- **Jam dengan rata-rata penyewaan tertinggi:** pukul 17.00, dengan rata-rata sekitar 461,45 penyewaan sepeda per jam.
- **Musim dengan rata-rata penyewaan harian tertinggi:** musim gugur (*Fall*, season 3), dengan rata-rata sekitar 5.644,30 penyewaan sepeda per hari.
- **Pola penyewaan berdasarkan jam:** rata-rata penyewaan cenderung lebih tinggi pada sore hari dan lebih rendah pada dini hari.

Temuan ini menunjukkan bahwa waktu dan musim dapat menjadi pertimbangan dalam perencanaan ketersediaan sepeda.

## Kesimpulan dan Rekomendasi

Analisis menunjukkan bahwa rata-rata penyewaan sepeda per jam mencapai nilai tertinggi pada pukul 17.00. Sementara itu, musim gugur (*Fall*, season 3) memiliki rata-rata penyewaan harian tertinggi dibandingkan musim lainnya.

Berdasarkan temuan tersebut, pengelola layanan sepeda disarankan untuk memperhatikan ketersediaan sepeda pada jam-jam dengan permintaan tinggi serta mempertimbangkan pola penyewaan antar musim dalam perencanaan operasional.

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

Dashboard Pedal Insights menyajikan ringkasan dan visualisasi data penyewaan sepeda berdasarkan jam, musim, dan kondisi cuaca. Dashboard juga menyediakan filter rentang tanggal agar pengguna dapat mengeksplorasi data pada periode tertentu.

Jika dashboard telah di-deploy, tautan akses dapat dicantumkan pada file `url.txt`.
