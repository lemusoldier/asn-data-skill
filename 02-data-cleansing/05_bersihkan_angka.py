#!/usr/bin/env python3
"""05 — Bersihkan Data Numerik
Contoh: kolom gaji ada yang pakai "Rp", koma, atau titik.
"""
import pandas as pd
import re

# Contoh data kotor (kolom gaji bermasalah)
data_gaji = [
    {"nama": "Budi Santoso", "gaji": "Rp 5.500.000"},
    {"nama": "Siti Rahayu", "gaji": "5,500,000"},
    {"nama": "Ahmad Hidayat", "gaji": "5500000"},
    {"nama": "Dewi Lestari", "gaji": "Rp4.500.000,-"},
    {"nama": "Rina Wati", "gaji": "6.000.000,00"},
]

df = pd.DataFrame(data_gaji)

print("=== DATA GAJI KOTOR ===")
print(df.to_string(index=False))
print()

# Fungsi bersihkan angka
def bersihkan_angka(teks):
    """Hapus semua karakter non-numeric kecuali titik desimal."""
    if pd.isna(teks):
        return 0
    teks = str(teks)
    # Hapus "Rp", spasi, koma, strip, ",-", dll
    teks = re.sub(r"[^\d.]", "", teks)
    # Handle koma sebagai pemisah ribuan (sudah dihapus)
    try:
        return int(float(teks))
    except ValueError:
        return 0

df["gaji_bersih"] = df["gaji"].apply(bersihkan_angka)

print("=== DATA GAJI BERSIH ===")
print(df.to_string(index=False))
print()
print(f"Total gaji : Rp {df['gaji_bersih'].sum():,.0f}")
print(f"Rata-rata  : Rp {df['gaji_bersih'].mean():,.0f}")
