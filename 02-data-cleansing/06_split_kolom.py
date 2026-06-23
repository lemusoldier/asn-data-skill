#!/usr/bin/env python3
"""06 — Pecah Kolom
Contoh: nama gabungan perlu dipecah jadi nama depan & nama belakang.
"""
import pandas as pd

data = [
    {"nama_lengkap": "Budi Santoso", "nip": "198501152010011004"},
    {"nama_lengkap": "Siti Rahayu Putri", "nip": "198803122012012003"},
    {"nama_lengkap": "Ahmad Hidayat", "nip": "199006012015011001"},
    {"nama_lengkap": "Dewi Lestari Wulandari", "nip": "199201252018012005"},
]

df = pd.DataFrame(data)

print("=== SEBELUM DIPECAH ===")
print(df.to_string(index=False))
print()

# Pecah nama: ambil kata pertama = nama depan, sisa = nama belakang
df["nama_depan"] = df["nama_lengkap"].str.split(n=1).str[0]
df["nama_belakang"] = df["nama_lengkap"].str.split(n=1).str[1].fillna("")

# Bonus: buat inisial dari nama depan + huruf pertama nama belakang
df["inisial"] = df["nama_depan"].str[0] + ". " + df["nama_belakang"].str[0].fillna("")

print("=== SESUDAH DIPECAH ===")
print(df.to_string(index=False))
print()

# Simpan
df.to_csv("nama_pecah.csv", index=False)
print("✅ Tersimpan: nama_pecah.csv")
