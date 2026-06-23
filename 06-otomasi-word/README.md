# 06 — Otomasi Pembuatan Surat Dinas

> Auto-generate dokumen Word (.docx) seperti surat dinas, SK, undangan, atau sertifikat berdasarkan data dari Excel/CSV.
> Tidak perlu lagi copas satu-satu pake Mail Merge yang ribet.

## Yang Dibutuhkan

```bash
pip install python-docx pandas
```

## Topik

| File | Fungsi | Contoh Kasus ASN |
|------|--------|-----------------|
| `01_generate_surat.py` | Generate surat dinas individu | Mengisi nama, NIP, alamat otomatis |
| `02_bulk_undangan.py` | Generate undangan rapat massal | Bikin 50 file undangan dalam 2 detik |
| `03_sk_generator.py` | Generate SK (Surat Keputusan) | Bikin SK mutasi/tugas dengan tabel dinamis |
