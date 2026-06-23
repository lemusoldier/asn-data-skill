#!/usr/bin/env python3
"""03 — Prediksi Usia Pensiun & Demografi Usia
Contoh: siapa yang akan pensiun dalam 5 tahun ke depan?
"""
import pandas as pd
from datetime import datetime

df = pd.read_csv("data_rekap.csv")

# Hitung usia sekarang (per 2026)
tahun_sekarang = 2026
df["tahun_lahir"] = pd.to_datetime(df["tanggal_lahir"]).dt.year
df["usia_sekarang"] = tahun_sekarang - df["tahun_lahir"]

# Batas pensiun = 58 tahun (PNS: 58 untuk pejabat admin, 60 untuk pejabat struktural)
batas_pensiun = 58
df["tahun_pensiun"] = df["tahun_lahir"] + batas_pensiun
df["sisa_kerja"] = df["tahun_pensiun"] - tahun_sekarang

print("=" * 65)
print("ANALISIS USIA & PREDIKSI PENSIUN")
print("=" * 65)
print()

# === Pensiun ≤ 5 tahun ===
pensiun_dekat = df[df["sisa_kerja"] <= 5]
print("--- AKAN PENSIUN ≤ 5 TAHUN ---")
if len(pensiun_dekat) > 0:
    for _, r in pensiun_dekat.iterrows():
        print(f"  {r['nama']:<20} | {r['usia_sekarang']} th | Pensiun: {r['tahun_pensiun']} ({r['sisa_kerja']} th lagi)")
else:
    print("  Tidak ada")
print()

# === Sebaran Usia ===
print("--- SEBARAN USIA ---")
bins = [0, 25, 30, 35, 40, 45, 50, 100]
labels = ["<25", "25-29", "30-34", "35-39", "40-44", "45-49", "50+"]
df["kelompok_usia"] = pd.cut(df["usia_sekarang"], bins=bins, labels=labels, right=False)
sebaran = df["kelompok_usia"].value_counts().sort_index()

for usia, jumlah in sebaran.items():
    bar = "#" * jumlah
    print(f"  {usia:<6}: {jumlah} orang {bar}")
print()

# Simpan ke Excel
df.to_excel("analisis_pensiun.xlsx", index=False)
print("✅ Tersimpan: analisis_pensiun.xlsx")
