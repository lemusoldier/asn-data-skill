#!/usr/bin/env python3
"""01 — Rekap Pegawai per Unit / Golongan
Contoh: berapa pegawai di tiap unit? Sebaran golongannya gimana?
"""
import pandas as pd

df = pd.read_csv("data_rekap.csv")

print("=" * 50)
print("REKAP PEGAWAI")
print("=" * 50)
print()

# === Per Unit Kerja ===
print("--- JUMLAH PEGAWAI PER UNIT ---")
rekap_unit = df["unit_kerja"].value_counts()
for unit, jumlah in rekap_unit.items():
    print(f"  {unit:<15}: {jumlah} orang")
print(f"  {'TOTAL':<15}: {len(df)} orang")
print()

# === Per Golongan ===
print("--- SEBARAN GOLONGAN ---")
rekap_gol = df["golongan"].value_counts().sort_index()
for gol, jumlah in rekap_gol.items():
    print(f"  Golongan {gol:<4}: {jumlah} orang")
print()

# === Unit x Golongan (Pivot Table) ===
print("--- TABEL SILANG (Unit x Golongan) ---")
pivot = pd.crosstab(df["unit_kerja"], df["golongan"])
print(pivot.to_string())
print()

# === Per Unit Lengkap ===
print("--- REKAP LENGKAP PER UNIT ---")
rekap_lengkap = df.groupby("unit_kerja").agg(
    jumlah=("nip", "count"),
    total_gaji=("gaji_pokok", "sum"),
    rata_gaji=("gaji_pokok", "mean"),
)
rekap_lengkap["rata_gaji"] = rekap_lengkap["rata_gaji"].round(0).astype(int)
print(rekap_lengkap.to_string())
print()

# Simpan ke Excel
rekap_lengkap.to_excel("rekap_pegawai.xlsx")
print("✅ Tersimpan: rekap_pegawai.xlsx")
