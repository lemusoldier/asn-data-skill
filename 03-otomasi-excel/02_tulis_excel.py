#!/usr/bin/env python3
"""02 — Tulis DataFrame ke Excel
Contoh: generate file laporan .xlsx dari data yang sudah diolah.
"""
import pandas as pd

data = {
    "nip": ["198501152010011004", "198803122012012003", "199006012015011001"],
    "nama": ["Budi Santoso", "Siti Rahayu", "Ahmad Hidayat"],
    "jabatan": ["Analis Kepegawaian", "Kepala Subbag", "Staff Umum"],
    "golongan": ["III/c", "IV/a", "III/b"],
    "gaji_pokok": [5_500_000, 6_200_000, 5_000_000],
}

df = pd.DataFrame(data)

# Tulis ke Excel
output_file = "laporan_pegawai.xlsx"
df.to_excel(output_file, index=False, sheet_name="Rekap Pegawai")

print(f"✅ File tersimpan: {output_file}")
print(f"   Baris : {len(df)}")
print(f"   Kolom : {len(df.columns)}")
print()

# Tulis ke beberapa sheet sekaligus
with pd.ExcelWriter("laporan_multi_sheet.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, index=False, sheet_name="Semua Pegawai")
    df[df["golongan"].str.startswith("III")].to_excel(writer, index=False, sheet_name="Golongan III")
    df[df["golongan"].str.startswith("IV")].to_excel(writer, index=False, sheet_name="Golongan IV")

print("✅ File multi-sheet tersimpan: laporan_multi_sheet.xlsx")
