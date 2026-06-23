#!/usr/bin/env python3
"""02 — Cek Range Angka (Outlier Detection)
Contoh: deteksi gaji atau usia yang tidak wajar.
"""
import pandas as pd

df = pd.read_csv("data_pegawai_validasi.csv")

print("=== CEK OUTLIER ===")
print()

# === CEK GAJI ===
print("--- Gaji Pokok ---")
gaji_median = df["gaji_pokok"].median()
batas_bawah = gaji_median * 0.5
batas_atas = gaji_median * 2.0

gaji_aneh = df[(df["gaji_pokok"] < batas_bawah) | (df["gaji_pokok"] > batas_atas)]

if len(gaji_aneh) > 0:
    print(f"Data mencurigakan (di luar Rp {batas_bawah:,.0f} - Rp {batas_atas:,.0f}):")
    for _, r in gaji_aneh.iterrows():
        print(f"  ❌ {r['nama']:<20} Rp {r['gaji_pokok']:>12,}")
else:
    print("✅ Semua gaji dalam range wajar")
print()

# === CEK USIA ===
print("--- Usia Pegawai ---")
usia_aneh = df[(df["usia"] < 17) | (df["usia"] > 70)]
print(f"Range wajar: 17 - 70 tahun")

if len(usia_aneh) > 0:
    for _, r in usia_aneh.iterrows():
        print(f"  ❌ {r['nama']:<20} {r['usia']} tahun")
else:
    print("✅ Semua usia dalam range wajar")
print()

# Ringkasan
print("=== RINGKASAN ===")
print(f"  Gaji:   min Rp {df['gaji_pokok'].min():>10,}, "
      f"max Rp {df['gaji_pokok'].max():>10,}, "
      f"median Rp {gaji_median:>10,}")
print(f"  Usia:   min {df['usia'].min()} th, "
      f"max {df['usia'].max()} th, "
      f"rata-rata {df['usia'].mean():.0f} th")
