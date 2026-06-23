#!/usr/bin/env python3
"""03 — Cek Inkonsistensi Data
Contoh: NIP sama tapi nama beda, atau nama sama tapi NIP beda.
"""
import pandas as pd

df = pd.read_csv("data_pegawai_validasi.csv")

print("=== CEK INKONSISTENSI ===")
print()

# === NAMA SAMA → Cek apakah NIP-nya sama ===
# (Standarisasi nama dulu biar fair)
df["nama_normal"] = df["nama"].str.strip().str.lower()

duplikasi_nama = df[df.duplicated(subset=["nama_normal"], keep=False)].sort_values("nama_normal")

if len(duplikasi_nama) > 0:
    print("❗ Nama ganda dengan data potensial berbeda:")
    for _, r in duplikasi_nama.iterrows():
        print(f"  {r['nama']:<20} | NIP: {r['nip']}")
else:
    print("✅ Tidak ada nama ganda")
print()

# === NIP SAMA → Cek apakah nama-nya sama ===
duplikasi_nip = df[df["nip"].duplicated(keep=False)].sort_values("nip")

if len(duplikasi_nip) > 0:
    print("❗ NIP ganda:")
    for _, r in duplikasi_nip.iterrows():
        print(f"  NIP: {r['nip']:<22} | {r['nama']:<20} | {r['golongan']}")
else:
    print("✅ Tidak ada NIP ganda")
print()

# === GOLONGAN vs GAJI ===
print("=== Cek Gaji per Golongan ===")
rata_gol = df.groupby("golongan")["gaji_pokok"].mean().round(0).astype(int)
for gol, avg in rata_gol.items():
    print(f"  Gol {gol:<4}: rata-rata gaji Rp {avg:>10,}")
