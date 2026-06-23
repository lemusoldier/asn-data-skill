#!/usr/bin/env python3
"""02 — Analisis Anggaran Gaji & Tunjangan
Contoh: total pengeluaran gaji per bulan, berapa besar tunjangan, dll.
"""
import pandas as pd

df = pd.read_csv("data_rekap.csv")

# Hitung tunjangan berdasarkan golongan (simulasi)
def hitung_tunjangan(gol):
    if gol.startswith("IV"):
        return 1_500_000
    elif gol.startswith("III"):
        return 1_000_000
    elif gol.startswith("II"):
        return 750_000
    else:
        return 500_000

df["tunjangan"] = df["golongan"].apply(hitung_tunjangan)
df["total_terima"] = df["gaji_pokok"] + df["tunjangan"]

print("=" * 60)
print("ANALISIS ANGGARAN GAJI & TUNJANGAN")
print("=" * 60)
print()

# === Total per Bulan ===
print(f"{'INDIKATOR':<35} {'NILAI':>15}")
print("-" * 60)
print(f"{'Total Gaji Pokok':<35} Rp {df['gaji_pokok'].sum():>12,}")
print(f"{'Total Tunjangan':<35} Rp {df['tunjangan'].sum():>12,}")
print(f"{'Total Penerimaan':<35} Rp {df['total_terima'].sum():>12,}")
print(f"{'Rata-rata Gaji':<35} Rp {df['gaji_pokok'].mean():>12,.0f}")
print(f"{'Rata-rata Tunjangan':<35} Rp {df['tunjangan'].mean():>12,.0f}")
print()

# === Per Unit ===
print("--- ANGGARAN PER UNIT ---")
anggaran = df.groupby("unit_kerja").agg(
    pegawai=("nip", "count"),
    total_gaji=("gaji_pokok", "sum"),
    total_tunjangan=("tunjangan", "sum"),
    total_penerimaan=("total_terima", "sum"),
)
print(anggaran.to_string())
print()

# Simpan ke Excel
df.to_excel("analisis_anggaran.xlsx", index=False)
print("✅ Tersimpan: analisis_anggaran.xlsx")
