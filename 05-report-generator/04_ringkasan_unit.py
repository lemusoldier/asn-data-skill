#!/usr/bin/env python3
"""04 — Ringkasan per Unit Kerja
Generate laporan ringkasan untuk tiap unit kerja dalam format rapi.
"""
import pandas as pd
from datetime import datetime

df = pd.read_csv("data_rekap.csv")

# =====================
# Ringkasan per Unit
# =====================
units = df["unit_kerja"].unique()

for unit in units:
    df_unit = df[df["unit_kerja"] == unit]

    print("=" * 50)
    print(f"RINGKASAN UNIT: {unit.upper()}")
    print(f"Generated: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("=" * 50)
    print()

    print(f"Jumlah pegawai   : {len(df_unit)}")
    print(f"Total gaji       : Rp {df_unit['gaji_pokok'].sum():>12,}")
    print(f"Rata-rata gaji   : Rp {df_unit['gaji_pokok'].mean():>12,.0f}")
    print(f"Gaji terendah    : Rp {df_unit['gaji_pokok'].min():>12,}")
    print(f"Gaji tertinggi   : Rp {df_unit['gaji_pokok'].max():>12,}")
    print()

    print("Daftar Pegawai:")
    print("-" * 50)
    for _, r in df_unit.iterrows():
        print(f"  {r['nama']:<20} | {r['golongan']:<4} | Rp {r['gaji_pokok']:>10,}")
    print()
    print()

# Simpan semua data ke satu file Excel dengan banyak sheet
with pd.ExcelWriter("ringkasan_all_unit.xlsx", engine="openpyxl") as writer:
    for unit in units:
        df_unit = df[df["unit_kerja"] == unit]
        df_unit.to_excel(writer, index=False, sheet_name=unit[:31])  # Excel max 31 chars

    # Sheet ringkasan
    rekap = df.groupby("unit_kerja").agg(
        jumlah=("nip", "count"),
        total_gaji=("gaji_pokok", "sum"),
        rata_gaji=("gaji_pokok", "mean"),
    ).reset_index()
    rekap.to_excel(writer, index=False, sheet_name="Ringkasan")

print("✅ Tersimpan: ringkasan_all_unit.xlsx (multi-sheet)")
