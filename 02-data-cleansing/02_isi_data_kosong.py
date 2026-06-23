#!/usr/bin/env python3
"""02 — Isi Data Kosong (Missing Values)
Contoh: data pegawai ada yang kolom NIP, jabatan, atau unit kosong.
"""
import pandas as pd

# Baca data (asumsi sudah hapus duplikat)
df = pd.read_csv("data_pegawai_bersih.csv")

print("=== CEK DATA KOSONG ===")
kosong = df.isnull().sum()
print(kosong[kosong > 0])
print()

# Isi data kosong dengan nilai yang masuk akal
# NIP kosong → tandai sebagai "PERLU DIPERBAIKI"
df["nip"] = df["nip"].fillna("PERLU DIPERBAIKI")

# Jabatan kosong → isi "Belum Ditentukan"
df["jabatan"] = df["jabatan"].fillna("Belum Ditentukan")

# Unit kerja kosong → isi "Belum Ditempatkan"
df["unit_kerja"] = df["unit_kerja"].fillna("Belum Ditempatkan")

print("=== SESUDAH DIISI ===")
kosong_sisa = df.isnull().sum()
print(f"Data kosong tersisa: {kosong_sisa.sum()} kolom")
print()

# Tampilkan baris yang tadinya kosong
print("=== Baris yang Tadinya Kosong ===")
print(df[["nama", "nip", "jabatan", "unit_kerja"]].to_string(index=False))
print()

# Simpan
df.to_csv("data_pegawai_bersih.csv", index=False)
print("✅ Tersimpan: data_pegawai_bersih.csv")
