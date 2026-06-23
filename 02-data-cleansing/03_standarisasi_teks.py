#!/usr/bin/env python3
"""03 — Standarisasi Teks
Contoh: nama & jabatan tidak konsisten (spasi awal/akhir, huruf campur).
"""
import pandas as pd

df = pd.read_csv("data_pegawai_bersih.csv")

print("=== SEBELUM DISTANDARISASI ===")
print("Nama unik:")
for n in df["nama"].unique():
    print(f"  [{n}]")
print()

# 1. Hapus spasi di awal dan akhir
df["nama"] = df["nama"].str.strip()

# 2. Standarisasi huruf: "BUDI SANTOSO" → "Budi Santoso"
df["nama"] = df["nama"].str.title()

# 3. Hapus spasi berlebih di tengah
df["nama"] = df["nama"].str.replace(r"\s+", " ", regex=True)

# 4. Standarisasi jabatan ke huruf kecil dulu, lalu title case
df["jabatan"] = df["jabatan"].str.strip().str.title()

# 5. Standarisasi unit kerja
df["unit_kerja"] = df["unit_kerja"].str.strip().str.title()

print("=== SESUDAH DISTANDARISASI ===")
print("Nama unik:")
for n in df["nama"].unique():
    print(f"  [{n}]")
print()

# Cek apakah "Ahmad Hidayat" dan "  Ahmad Hidayat " sudah jadi satu nama
jumlah_ahmad = len(df[df["nama"].str.contains("Ahmad Hidayat")])
print(f"'Ahmad Hidayat' muncul {jumlah_ahmad}x (setelah standarisasi)")
print()

df.to_csv("data_pegawai_bersih.csv", index=False)
print("✅ Tersimpan: data_pegawai_bersih.csv")
