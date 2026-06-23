#!/usr/bin/env python3
"""04 — Laporan Validasi Data Otomatis
Generate ringkasan validasi data dalam satu file laporan.
"""
import pandas as pd
from datetime import datetime

df = pd.read_csv("data_pegawai_validasi.csv")

# === BUAT RINGKASAN ===
laporan = []
laporan.append("=" * 60)
laporan.append("LAPORAN VALIDASI DATA PEGAWAI")
laporan.append(f"Tanggal: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
laporan.append(f"Sumber  : data_pegawai_validasi.csv")
laporan.append("=" * 60)
laporan.append("")

# 1. Statistik dasar
laporan.append(f"1. STATISTIK DASAR")
laporan.append(f"   Total baris        : {len(df)}")
laporan.append(f"   Total NIP unik     : {df['nip'].nunique()}")
laporan.append(f"   Total nama unik    : {df['nama'].nunique()}")
laporan.append("")

# 2. Cek NIP
nip_bermasalah = 0
for i, row in df.iterrows():
    nip = str(row["nip"]).strip()
    if not (len(nip) == 18 and nip.isdigit()):
        nip_bermasalah += 1

laporan.append(f"2. VALIDASI NIP")
laporan.append(f"   Valid                : {len(df) - nip_bermasalah}")
laporan.append(f"   Bermasalah           : {nip_bermasalah}")
laporan.append("")

# 3. Cek data kosong
kosong = df.isnull().sum()
kolom_kosong = kosong[kosong > 0]
if len(kolom_kosong) > 0:
    laporan.append(f"3. DATA KOSONG")
    for k, v in kolom_kosong.items():
        laporan.append(f"   {k:<20}: {v} baris")
    laporan.append("")

# 4. Cek outlier gaji
gaji_median = df["gaji_pokok"].median()
batas_atas = gaji_median * 2
outlier = len(df[df["gaji_pokok"] > batas_atas])

laporan.append(f"4. OUTLIER DETEKSI")
laporan.append(f"   Gaji > Rp {batas_atas:,.0f}: {outlier} pegawai")
laporan.append("")

# 5. Distribusi golongan
laporan.append(f"5. DISTRIBUSI GOLONGAN")
for gol, count in df["golongan"].value_counts().sort_index().items():
    laporan.append(f"   Golongan {gol:<4}: {count} orang")
laporan.append("")

laporan.append("=" * 60)
laporan.append("AKSI YANG DISARANKAN:")
laporan.append("  ❌ Perbaiki NIP bermasalah")
if nip_bermasalah > 0:
    laporan.append("  ❌ Periksa data duplikat/inkonsisten")
laporan.append("  ✅ Validasi rutin dijalankan setiap bulan")
laporan.append("=" * 60)

# Tampilkan
for line in laporan:
    print(line)

# Simpan ke file teks
with open("laporan_validasi.txt", "w") as f:
    f.write("\n".join(laporan))

print(f"✅ Tersimpan: laporan_validasi.txt")
