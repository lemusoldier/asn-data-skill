# 02 — Data Cleansing dengan Python

> Script-script untuk membersihkan data mentah sebelum diolah.
> Cocok untuk data kepegawaian, data SPTJM, data rekapitulasi, dll.

## Yang Dibutuhkan

```bash
pip install pandas openpyxl
```

## Topik

| File | Fungsi | Contoh Kasus ASN |
|------|--------|-----------------|
| `01_hapus_duplikat.py` | Hapus data duplikat | Rekap NIP ganda dari 2 sistem |
| `02_isi_data_kosong.py` | Isi missing values | Data pegawai kolom kosong |
| `03_standarisasi_teks.py` | Standardisasi teks | Nama & jabatan tidak konsisten |
| `04_konversi_tanggal.py` | Konversi format tanggal | Tanggal lahir berbagai format |
| `05_bersihkan_angka.py` | Bersihkan data numerik | Gaji/angka dengan karakter aneh |
| `06_split_kolom.py` | Pecah kolom menjadi beberapa | Nama gabungan / NIP terpisah |
| `07_merge_data.py` | Gabungkan beberapa file | Rekap dari beberapa unit |

## Cara Jalankan

```bash
# Jalankan satu per satu
python 01_hapus_duplikat.py

# Atau jalankan semua sekaligus
python -m 01_hapus_duplikat
```
