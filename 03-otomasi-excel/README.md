# 03 — Otomasi Excel dengan Python

> Baca, tulis, merge, dan format file Excel secara otomatis.
> Cocok untuk rekapitulasi bulanan, merge file unit kerja, format laporan.

## Yang Dibutuhkan

```bash
pip install pandas openpyxl xlsxwriter
```

## Topik

| File | Fungsi | Contoh Kasus ASN |
|------|--------|-----------------|
| `01_baca_excel.py` | Baca file .xlsx → pandas | Baca data dari sistem kepegawaian |
| `02_tulis_excel.py` | Tulis DataFrame → .xlsx | Generate laporan ke Excel |
| `03_merge_excel.py` | Gabung beberapa sheet/file | Merge rekap 3 unit kerja |
| `04_format_laporan.py` | Format Excel otomatis | Bold, warna, border, lebar kolom |
| `05_filter_export.py` | Filter data → export | Filter pegawai tertentu → export |

## Contoh Kasus

> *"Setiap bulan, admin kepegawaian harus merge 5 file Excel dari 5 bidang jadi 1 file rekap.
> Dengan script ini, proses itu selesai dalam hitungan detik."*
