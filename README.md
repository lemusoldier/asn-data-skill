# 📊 ASN Data Skill

> Repositori belajar pengolahan data untuk Aparatur Sipil Negara — Excel, Python, & Aplikasi Web.

---

## 🗺️ Peta Belajar

```
                     ASN DATA SKILL
                         │
          ┌──────────────┴──────────────┐
          │              │              │
     📗 TRACK EXCEL  🐍 TRACK PYTHON  🌐 WEB APP
          │              │              │
    ┌─────┼─────┐  ┌─────┼─────┐    07-
  Level  Level  Level  01-02-03-  Aplikasi
    1      2      3  DasarCleans. Streamlit
                          04-05-      │
                          Valid.Rep.  ▼
                             │     Dashboard
                          06-      Interaktif
                        Otomasi
                        Word
```

---

## 📗 Track Excel — Silabus Belajar

### Level 1: Fondasi — Kuasai Dasar
> **Untuk siapa:** Pemula yang baru kenal Excel.
> **Hasil:** Bisa input data rapi, filter, sort, dan pakai rumus dasar.

| # | Skill | Fungsi Penting | Video (YouTube/TikTok) |
|---|-------|----------------|------------------------|
| 1 | **Data Cleaning** | Filter, Sort, Remove Duplicates, Flash Fill | [Tutorial Olah Data Sederhana](https://www.youtube.com/watch?v=Klj_4Bi2jzU) \| [Tips Admin (TikTok)](https://www.tiktok.com/@excel.indonesia/video/7208527660257971483) |
| 2 | **Formula Dasar** | SUM, AVERAGE, COUNT, MAX, MIN | [30 Rumus Excel Untuk Admin](https://www.youtube.com/watch?v=VwKMgt5yVVM) \| [Tips Mba Excel (TikTok)](https://www.tiktok.com/@mba_excel/video/7629896666748947732) |
| 3 | **Logical IF** | IF, SUMIF, COUNTIF, IFS | ["IF": Mengolah Data dengan Syarat](https://www.youtube.com/watch?v=oIUGlnNy0MM) \| [Kursus ASN Berpijar](https://asn.futureskills.id/fs/aktivitas/kelas-async/52/public) |
| 4 | **Format & Visual** | Conditional Formatting, Highlight rules | [Tutorial Lengkap Formatting](https://www.youtube.com/watch?v=P3TMzADxLm0) |

### Level 2: Intermediate — Olah Data Teks & Relasi
> **Untuk siapa:** Staf yang sering menggabungkan data dari berbagai unit. 
> **Hasil:** Bisa rapikan teks yang berantakan, dan cari data antar file.

| # | Skill | Fungsi Penting | Video (YouTube/TikTok) |
|---|-------|----------------|------------------------|
| 5 | **Manipulasi Teks** | CONCAT, TEXTJOIN, SUBSTITUTE, TRIM, UPPER/LOWER | [Tutorial TEXTJOIN & CONCAT](https://www.youtube.com/watch?v=XzW3hFz2w0s) \| [Fungsi TRIM & SUBSTITUTE](https://www.youtube.com/watch?v=VwKMgt5yVVM) |
| 6 | **Lookup & Relasi** | VLOOKUP, HLOOKUP, XLOOKUP, INDEX+MATCH | [VLOOKUP vs XLOOKUP](https://www.youtube.com/watch?v=UIfrgw4wD9k) \| [XLOOKUP (TikTok)](https://www.tiktok.com/@era_dotcom/video/7560170046400548108) |
| 7 | **Pivot Table** | Pivot Table, Slicers, Calculated Fields | [Belajar Pivot Table Pemula → Mahir](https://www.youtube.com/watch?v=KWEr_L0LqWQ) |
| 8 | **Date & Time** | DATEDIF, NETWORKDAYS, EOMONTH, EDATE | [Rumus Tanggal Lengkap](https://www.youtube.com/watch?v=OYhDTWZn8pQ) |

### Level 3: Advanced — Analisis Lanjut & Otomasi
> **Untuk siapa:** Pengguna mahir / Admin Kepegawaian & Keuangan.
> **Hasil:** Bisa hitung matriks kompleks, bikin dashboard, Power Query.

| # | Skill | Fungsi Penting | Video (YouTube/TikTok) |
|---|-------|----------------|------------------------|
| 9 | **Analisis Array** | SUMPRODUCT (sangat berguna untuk rekap anggaran berdasar kriteria ganda) | [Cara Ampuh Pakai SUMPRODUCT](https://www.youtube.com/watch?v=Q4V2aY7oO4M) |
| 10 | **Data Validation** | Dropdown list, validasi NIP bersyarat | [Data Validation Excel](https://www.youtube.com/watch?v=jk4jVKl0D14) |
| 11 | **Power Query** | Import & transformasi otomatis ribuan baris | [Power Query Excel](https://www.youtube.com/watch?v=PQVKiLmW9DI) |
| 12 | **Dashboard** | Charts, Data Model, Relasi antar tabel | [Membuat Dashboard Excel](https://www.youtube.com/watch?v=9h7fdDrK6Dk) |

### 🧾 Program Resmi ASN (Wajib Cek)
- [ASN Future Skills — Mengelola Pendataan](https://asn.futureskills.id/fs/aktivitas/kelas-async/52/public) (Kolaborasi LAN & Pijar, GRATIS + Sertifikat)

---

## 🐍 Track Python — Silabus Belajar

> **Note:** Gunakan editor seperti VS Code atau PyCharm agar lebih nyaman. Jika tidak mau coding, buka folder `07-aplikasi-web/`.

| No | Folder | Topik | Kasus Penggunaan (Use Case) ASN |
|----|--------|-------|---------------------------------|
| 01 | [`01-python-dasar/`](./01-python-dasar/) | **Python Dasar** | Fondasi awal: variabel, kondisi, loop. |
| 02 | [`02-data-cleansing/`](./02-data-cleansing/) | **Data Cleansing** | Hapus NIP ganda, isi data kosong, standarisasi nama (huruf besar/kecil). |
| 03 | [`03-otomasi-excel/`](./03-otomasi-excel/) | **Otomasi Excel** | Merge otomatis file Excel laporan bulanan dari 5 bidang berbeda jadi 1 rekap. |
| 04 | [`04-data-validation/`](./04-data-validation/) | **Validasi Data** | Cek otomatis NIP bermasalah (bukan 18 digit) dan deteksi anomali usia pegawai. |
| 05 | [`05-report-generator/`](./05-report-generator/) | **Report Generator** | Prediksi siapa yang pensiun 5 tahun ke depan; hitung otomatis beban tunjangan/gaji per unit. |
| 06 | [`06-otomasi-word/`](./06-otomasi-word/) | **Otomasi Word** | Bikin 100 lembar surat dinas / undangan rapat / SPPD langsung dari 1 file Excel (Mail Merge Python). |
| 07 | [`07-aplikasi-web/`](./07-aplikasi-web/) | **Web Dashboard** | Aplikasi web tinggal pakai (Upload Excel → Clean/Merge → Download). Ramah buat staf non-IT! |

---

## 🎯 Tabel Solusi Praktis

Sedang buru-buru? Cari masalahmu di sini dan buka script yang sesuai:

| Masalah / Keluhan | Solusi Script | Buka Folder |
|-------------------|---------------|-------------|
| "NIP ganda, bingung cara hapusnya!" | `01_hapus_duplikat.py` | `02-data-cleansing/` |
| "NIP banyak yang nyasar 17 digit atau huruf!" | `01_cek_nip_valid.py` | `04-data-validation/` |
| "Harus ngirim SPPD ke 50 orang, capek kopas nama." | `02_bulk_undangan.py` | `06-otomasi-word/` |
| "Mau rekap pegawai per golongan buat laporan LAKIP." | `01_rekap_pegawai.py` | `05-report-generator/` |
| "Staf gue nggak ngerti koding, maunya tinggal klik-klik aja." | `app.py` (Jalankan web-nya) | `07-aplikasi-web/` |

---

## 📚 Channel Rekomendasi

| Channel | Platform | Fokus Konten |
|---------|----------|--------------|
| Excel Indonesia | [TikTok](https://www.tiktok.com/@excel.indonesia) | Tips jalan pintas Excel cepat |
| Mba Excel | [TikTok](https://www.tiktok.com/@mba_excel) | Tutorial kasus khusus pekerjaan Admin |
| Era Dotcom | [TikTok](https://www.tiktok.com/@era_dotcom) | Penggunaan rumus-rumus terbaru (XLOOKUP dll) |
| Ignasius Ryan | [YouTube](https://www.youtube.com/watch?v=VwKMgt5yVVM) | Penjelasan mendalam + contoh kasus perkantoran |
| Belajar Excel | [YouTube](https://www.youtube.com/watch?v=KWEr_L0LqWQ) | Tutorial spesifik alat berat Excel (Pivot, Power Query) |

---

## 🤝 Kontribusi

Punya script Python atau tutorial Excel yang sering menyelamatkan hidupmu di kantor? Submit PR!

1. Fork repo
2. Tambahkan di folder yang sesuai
3. Update README.md
4. Submit Pull Request

---

*Dibuat untuk membantu kemudahan administrasi ASN Indonesia 🇮🇩*
