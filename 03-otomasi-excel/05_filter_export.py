#!/usr/bin/env python3
"""05 — Filter Data & Export
Contoh: filter pegawai tertentu lalu export ke file terpisah.
"""
import pandas as pd

data = {
    "nip": ["198501152010011004", "198803122012012003", "199006012015011001",
            "199201252018012005", "198601252013012008", "198403102009011005"],
    "nama": ["Budi Santoso", "Siti Rahayu", "Ahmad Hidayat",
             "Dewi Lestari", "Lina Marlina", "Agus Suharto"],
    "golongan": ["III/c", "IV/a", "III/b", "III/a", "IV/b", "IV/a"],
    "gaji_pokok": [5_500_000, 6_200_000, 5_000_000, 4_500_000, 6_500_000, 7_000_000],
    "unit": ["Kepegawaian", "Kepegawaian", "Umum", "Keuangan", "Umum", "Keuangan"],
}

df = pd.DataFrame(data)

print("=== SEMUA DATA ===")
print(f"Total: {len(df)} pegawai")
print()

# Filter 1: Pegawai Golongan IV ke atas
df_gol_iv = df[df["golongan"].str.startswith("IV")]
df_gol_iv.to_excel("filter_golongan_IV.xlsx", index=False)
print(f"✅ Filter Gol IV  : {len(df_gol_iv)} orang → filter_golongan_IV.xlsx")

# Filter 2: Pegawai Gaji di atas 5 juta
df_gaji = df[df["gaji_pokok"] > 5_000_000]
df_gaji.to_excel("filter_gaji_diatas_5jt.xlsx", index=False)
print(f"✅ Filter Gaji >5jt: {len(df_gaji)} orang → filter_gaji_diatas_5jt.xlsx")

# Filter 3: Per unit kerja
for unit in df["unit"].unique():
    df_unit = df[df["unit"] == unit]
    nama_file = f"rekap_unit_{unit.lower()}.xlsx"
    df_unit.to_excel(nama_file, index=False)
    print(f"✅ Unit {unit:<15}: {len(df_unit)} orang → {nama_file}")

print()
print("Selesai! Semua filter sudah di-export ke file terpisah.")
