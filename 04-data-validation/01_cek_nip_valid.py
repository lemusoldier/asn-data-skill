#!/usr/bin/env python3
"""01 — Validasi Format NIP
Aturan NIP ASN: 18 digit angka.
"""
import pandas as pd
import re

df = pd.read_csv("data_pegawai_validasi.csv")

print("=== CEK FORMAT NIP ===")
print()

nip_bermasalah = []
for i, row in df.iterrows():
    nip = str(row["nip"]).strip()
    # Rule: NIP harus 18 digit angka
    if not re.match(r"^\d{18}$", nip):
        nip_bermasalah.append({
            "no": i + 1,
            "nama": row["nama"],
            "nip": nip,
            "masalah": f"{len(nip)} digit, bukan 18"
        })

if nip_bermasalah:
    print(f"Ditemukan {len(nip_bermasalah)} NIP bermasalah:")
    print("-" * 60)
    for n in nip_bermasalah:
        print(f"  {n['no']}. {n['nama']:<20} NIP: [{n['nip']}] — {n['masalah']}")
else:
    print("✅ Semua NIP valid!")

print()

# Output ringkasan
total = len(df)
valid = total - len(nip_bermasalah)
print(f"Ringkasan:")
print(f"  Data      : {total} baris")
print(f"  NIP valid : {valid} ({valid/total*100:.0f}%)")
print(f"  Bermasalah: {len(nip_bermasalah)} ({len(nip_bermasalah)/total*100:.0f}%)")
