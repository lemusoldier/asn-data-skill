#!/usr/bin/env python3
"""04 — Konversi Format Tanggal
Contoh: data dari berbagai sumber pakai format tanggal beda-beda.
"""
import pandas as pd

df = pd.read_csv("data_pegawai_bersih.csv")

print("=== FORMAT TANGGAL SEBELUM ===")
print(df[["nama", "tanggal_lahir"]].to_string(index=False))
print()

# Konversi semua format tanggal ke format standar YYYY-MM-DD
df["tanggal_lahir"] = pd.to_datetime(df["tanggal_lahir"], format="mixed", dayfirst=False)

# Format ke string YYYY-MM-DD
df["tanggal_lahir"] = df["tanggal_lahir"].dt.strftime("%Y-%m-%d")

# Tambah kolom tahun lahir (berguna untuk filter / perhitungan)
df["tahun_lahir"] = pd.to_datetime(df["tanggal_lahir"]).dt.year

# Tambah kolom usia (per tahun 2026)
tahun_sekarang = 2026
df["usia"] = tahun_sekarang - df["tahun_lahir"]

print("=== FORMAT TANGGAL SESUDAH ===")
print(df[["nama", "tanggal_lahir", "tahun_lahir", "usia"]].to_string(index=False))
print()

# Simpan
df.to_csv("data_pegawai_bersih.csv", index=False)
print("✅ Tersimpan: data_pegawai_bersih.csv")
