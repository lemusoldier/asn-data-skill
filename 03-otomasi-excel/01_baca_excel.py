#!/usr/bin/env python3
"""01 — Baca File Excel
Contoh: membaca data dari file .xlsx yang di-export dari sistem.
"""
import pandas as pd

# Baca dari CSV (bisa juga .xlsx dengan pd.read_excel)
df = pd.read_csv("data_unit_1.csv")

print("=== DATA UNIT KERJA 1 ===")
print(f"Jumlah baris : {len(df)}")
print(f"Kolom        : {list(df.columns)}")
print()
print(df.to_string(index=False))
print()

# Akses data tertentu
print("=== AKSES DATA ===")
print(f"Pegawai pertama  : {df.iloc[0]['nama']}")
print(f"Total gaji       : Rp {df['gaji_pokok'].sum():,.0f}")
print()

# Baca file Excel (.xlsx)
# df_excel = pd.read_excel("file_dari_sistem.xlsx", sheet_name="Sheet1")
# df_excel = pd.read_excel("file_dari_sistem.xlsx", sheet_name="Rekap")
# print(f"Jumlah sheet tersedia: {pd.ExcelFile('file_dari_sistem.xlsx').sheet_names}")
