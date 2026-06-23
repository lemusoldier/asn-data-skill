#!/usr/bin/env python3
"""01 — Hapus Data Duplikat
Contoh: rekap dari 2 sistem menghasilkan data NIP yang sama lebih dari sekali.
"""
import pandas as pd

# Baca data mentah
df = pd.read_csv("data_pegawai_mentah.csv")

print("=== SEBELUM DIBERSIHKAN ===")
print(f"Total baris : {len(df)}")
print(f"Unik NIP    : {df['nip'].nunique()}")
print(f"Duplikat    : {df.duplicated(subset=['nip']).sum()} baris")
print()

# Hapus duplikat berdasarkan NIP (pertama muncul dianggap benar)
df_bersih = df.drop_duplicates(subset=["nip"], keep="first")

print("=== SESUDAH DIBERSIHKAN ===")
print(f"Total baris : {len(df_bersih)}")
print(f"Dihapus     : {len(df) - len(df_bersih)} baris duplikat")
print()

# Tampilkan hasil
print(df_bersih[["nama", "nip", "jabatan"]].to_string(index=False))
print()

# Simpan hasil
df_bersih.to_csv("data_pegawai_bersih.csv", index=False)
print("✅ Tersimpan: data_pegawai_bersih.csv")
