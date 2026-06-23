#!/usr/bin/env python3
"""07 — Gabungkan Beberapa File
Contoh: data pegawai dari 3 unit kerja terpisah perlu digabung jadi satu rekap.
"""
import pandas as pd
import os

# Buat contoh data 3 unit kerja
unit_kepegawaian = pd.DataFrame({
    "nip": ["198501152010011004", "198803122012012003"],
    "nama": ["Budi Santoso", "Siti Rahayu"],
    "jabatan": ["Analis Kepegawaian", "Kepala Subbag"],
    "unit": ["Kepegawaian", "Kepegawaian"],
})

unit_keuangan = pd.DataFrame({
    "nip": ["199006012015011001", "199201252018012005"],
    "nama": ["Ahmad Hidayat", "Dewi Lestari"],
    "jabatan": ["Staff Keuangan", "Staff Keuangan"],
    "unit": ["Keuangan", "Keuangan"],
})

unit_umum = pd.DataFrame({
    "nip": ["198601252013012008", "198403102009011005"],
    "nama": ["Lina Marlina", "Agus Suharto"],
    "jabatan": ["Sekretaris", "Kabag Umum"],
    "unit": ["Umum", "Umum"],
})

print("=== DATA DARI 3 UNIT KERJA ===")
print(f"Kepegawaian : {len(unit_kepegawaian)} pegawai")
print(f"Keuangan    : {len(unit_keuangan)} pegawai")
print(f"Umum        : {len(unit_umum)} pegawai")
print()

# Gabungkan semua
semua_unit = pd.concat([unit_kepegawaian, unit_keuangan, unit_umum], ignore_index=True)

# Urutkan berdasarkan NIP
semua_unit = semua_unit.sort_values("nip").reset_index(drop=True)

print("=== HASIL GABUNGAN ===")
print(f"Total : {len(semua_unit)} pegawai")
print()
print(semua_unit.to_string(index=False))
print()

# Simpan
semua_unit.to_csv("rekap_semua_unit.csv", index=False)
print("✅ Tersimpan: rekap_semua_unit.csv")
