#!/usr/bin/env python3
"""03 — Merge Beberapa File Excel
Contoh: gabungkan data dari 3 unit kerja jadi 1 rekap.
Skenario nyata: admin kepegawaian menerima data per bidang setiap bulan.
"""
import pandas as pd
import glob

# Baca semua file CSV dari folder (bisa juga .xlsx)
file_list = ["data_unit_1.csv", "data_unit_2.csv", "data_unit_3.csv"]

print(f"=== MERGE {len(file_list)} FILE ===")
print(f"File yang diproses: {file_list}")
print()

# Gabungkan semua file
df_list = []
for f in file_list:
    df = pd.read_csv(f)
    df_list.append.append(df)
    print(f"  ✅ {f}: {len(df)} baris")

df_gabungan = pd.concat(df_list, ignore_index=True)
df_gabungan = df_gabungan.sort_values("nip").reset_index(drop=True)

print()
print("=== HASIL GABUNGAN ===")
print(f"Total pegawai: {len(df_gabungan)}")
print(df_gabungan.to_string(index=False))
print()

# Simpan
output = "rekap_semua_unit.xlsx"
df_gabungan.to_excel(output, index=False, sheet_name="Rekap Gabungan")
print(f"✅ Tersimpan: {output}")

# Alternatif: merge dengan glob (semua file csv di folder)
# semua_file = glob.glob("data_unit_*.csv")
# df_gabungan = pd.concat([pd.read_csv(f) for f in semua_file], ignore_index=True)
