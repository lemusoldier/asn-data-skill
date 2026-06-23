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

| # | Skill | Video (YouTube/TikTok) |
|---|-------|----------------------|
| 1 | **Data Cleaning** — Filter, Sort, Remove Duplicates, Text-to-Columns | [Tutorial Olah Data Sederhana](https://www.youtube.com/watch?v=Klj_4Bi2jzU) \| [Tips Admin (TikTok)](https://www.tiktok.com/@excel.indonesia/video/7208527660257971483) |
| 2 | **Formula Dasar** — SUM, AVERAGE, COUNT, MAX, MIN | [30 Rumus Excel Untuk Admin](https://www.youtube.com/watch?v=VwKMgt5yVVM) \| [Tips Mba Excel (TikTok)](https://www.tiktok.com/@mba_excel/video/7629896666748947732) |
| 3 | **Logical IF** — IF, SUMIF, COUNTIF | ["IF": Mengolah Data dengan Syarat Tertentu](https://www.youtube.com/watch?v=oIUGlnNy0MM) \| [Kursus ASN Berpijar](https://asn.futureskills.id/fs/aktivitas/kelas-async/52/public) |
| 4 | **Conditional Formatting** — Warna otomatis, highlight rules | [Conditional Formatting — Tutorial Lengkap](https://www.youtube.com/watch?v=P3TMzADxLm0) |

### Level 2: Intermediate — Olah Data Lebih Cepat
> **Untuk siapa:** Yang sudah bisa rumus dasar.
> **Hasil:** Bisa pakai VLOOKUP, Pivot Table, dan fungsi tanggal.

| # | Skill | Video (YouTube/TikTok) |
|---|-------|----------------------|
| 5 | **VLOOKUP & XLOOKUP** — Cari data antar tabel | [Belajar VLOOKUP vs HLOOKUP vs XLOOKUP](https://www.youtube.com/watch?v=UIfrgw4wD9k) \| [XLOOKUP (TikTok)](https://www.tiktok.com/@era_dotcom/video/7560170046400548108) |
| 6 | **Pivot Table** — Meringkas ribuan baris data | [Belajar Pivot Table Pemula → Mahir](https://www.youtube.com/watch?v=KWEr_L0LqWQ) |
| 7 | **Date & Time Functions** — DATEDIF, NETWORKDAYS, EOMONonth | [Rumus Tanggal Excel Lengkap](https://www.youtube.com/watch?v=OYhDTWZn8pQ) |
| 8 | **Data Validation** — Dropdown list, input validation | [Data Validation di Excel](https://www.youtube.com/watch?v=jk4jVKl0D14) |

### Level 3: Advanced — Analisis & Otomasi
> **Untuk siapa:** Yang ingin jadi advanced user.
> **Hasil:** Bisa bikin dashboard, Power Query, dan otomatisasi.

| # | Skill | Video (YouTube/TikTok) |
|---|-------|----------------------|
| 9 | **Power Query** — Import & transformasi data otomatis | [Power Query Excel — Tutorial Lengkap](https://www.youtube.com/watch?v=PQVKiLmW9DI) |
| 10 | **Charts & Dashboard** — Visualisasi data profesional | [Membuat Dashboard Excel](https://www.youtube.com/watch?v=9h7fdDrK6Dk) |
| 11 | **Data Model & Relationship** — Hubungkan beberapa tabel | [Data Model di Excel](https://www.youtube.com/watch?v=lajpQnl0lWs) |

### 🧾 Program Resmi ASN
- [ASN Future Skills — Mengelola Pendataan dengan Excel](https://asn.futureskills.id/fs/aktivitas/kelas-async/52/public) — Kolaborasi LAN & Pijar Foundation (GRATIS + Sertifikat)

---

## 🐍 Track Python — Silabus Belajar

| No | Folder | Topik | Deskripsi |
|----|--------|-------|-----------|
| 01 | [`01-python-dasar/`](./01-python-dasar/) | **Python Dasar** | Pengenalan Python: variabel, kondisi, loop, list/dict |
| 02 | [`02-data-cleansing/`](./02-data-cleansing/) | **Data Cleansing** | Bersihkan data mentah: hapus duplikat, isi data kosong, standarisasi |
| 03 | [`03-otomasi-excel/`](./03-otomasi-excel/) | **Otomasi Excel** | Baca, tulis, merge, format file Excel otomatis |
| 04 | [`04-data-validation/`](./04-data-validation/) | **Validasi Data** | Cek NIP, range gaji, inkonsistensi, laporan validasi |
| 05 | [`05-report-generator/`](./05-report-generator/) | **Report Generator** | Generate rekap pegawai, analisis anggaran, prediksi pensiun |
| 06 | [`06-otomasi-word/`](./06-otomasi-word/) | **Otomasi Surat Dinas** | Auto-generate .docx (surat dinas, undangan, SK) dari data Excel |
| 07 | [`07-aplikasi-web/`](./07-aplikasi-web/) | **Dashboard Web (Streamlit)** | Aplikasi visual untuk cleansing, merge, dan visualisasi data |

### Cara Mulai Track Python

```bash
# 1. Install library yang dibutuhkan
pip install pandas openpyxl python-docx streamlit

# 2. Clone repo ini
git clone git@github.com:lemusoldier/asn-data-skill.git
cd asn-data-skill

# 3. Mulai dari folder 01-python-dasar/
cd 01-python-dasar
python 01_hello.py

# 4. Jalankan Dashboard Web
cd ../07-aplikasi-web
streamlit run app.py
```

---

## 🎯 Contoh Kasus Nyata

| Masalah | Solusi | Script |
|---------|--------|--------|
| Rekap dari 3 unit → 1 file | Merge otomatis | `03-otomasi-excel/03_merge_excel.py` |
| Data dari sistem kotor (nama ga rapi, spasi) | Data cleansing batch | `02-data-cleansing/03_standarisasi_teks.py` |
| Cek NIP bermasalah sebelum upload ke BKN | Validasi NIP | `04-data-validation/01_cek_nip_valid.py` |
| Laporan bulanan rekap pegawai | Generate report | `05-report-generator/01_rekap_pegawai.py` |
| Filter pegawai gol IV → export | Filter + export | `03-otomasi-excel/05_filter_export.py` |
| Buat undangan rapat massal (50 nama) | Generate Word massal | `06-otomasi-word/02_bulk_undangan.py` |
| Rekan kerja butuh tool cleansing tanpa coding | Dashboard web | `07-aplikasi-web/app.py` |

---

## 📚 Channel Rekomendasi

| Channel | Platform | Konten |
|---------|----------|--------|
| Excel Indonesia | [TikTok](https://www.tiktok.com/@excel.indonesia) | Tips Excel singkat |
| Mba Excel | [TikTok](https://www.tiktok.com/@mba_excel) | Tutorial Admin |
| Era Dotcom | [TikTok](https://www.tiktok.com/@era_dotcom) | Rumus modern Excel |
| Ignasius Ryan | YouTube | [30 Rumus Excel Admin](https://www.youtube.com/watch?v=VwKMgt5yVVM) |
| Belajar Excel | YouTube | [Pivot Table](https://www.youtube.com/watch?v=KWEr_L0LqWQ) |
| ASN Berpijar | [Web](https://asn.futureskills.id/fs) | Kursus resmi gratis |

---

## 🤝 Kontribusi

Punya script Python atau tutorial Excel yang berguna? Submit PR!

1. Fork repo
2. Tambahkan di folder yang sesuai
3. Update README.md
4. Submit Pull Request

---

*Dibuat untuk membantu ASN Indonesia 🇮🇩*
