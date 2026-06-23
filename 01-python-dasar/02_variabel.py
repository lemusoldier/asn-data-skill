#!/usr/bin/env python3
"""02 — Tipe Data & Variabel
Memahami tipe data yang umum dipakai untuk mengolah data ASN.
"""

# === Tipe Data Dasar ===
nama = "Andi Prasetyo"          # string (teks)
nip = "199003012015011003"      # string (NIP harus string, bukan angka!)
umur = 35                       # integer (bilangan bulat)
tinggi = 170.5                  # float (bilangan desimal)
aktif = True                    # boolean (benar/salah)

print("=== Tipe Data ===")
print(f"Nama      : {nama} (tipe: {type(nama).__name__})")
print(f"NIP       : {nip} (tipe: {type(nip).__name__})")
print(f"Umur      : {umur} (tipe: {type(umur).__name__})")
print(f"Tinggi    : {tinggi} (tipe: {type(tinggi).__name__})")
print(f"Aktif     : {aktif} (tipe: {type(aktif).__name__})")
print()

# === Konversi Tipe Data ===
gaji_string = "8500000"
gaji_angka = int(gaji_string)  # string → integer
gaji_formatted = f"Rp {gaji_angka:,.0f}"  # format ribuan

print("=== Konversi Tipe Data ===")
print(f"Gaji (string)   : {gaji_string}")
print(f"Gaji (angka)    : {gaji_angka}")
print(f"Gaji (format)   : {gaji_formatted}")
print()

# === Operasi Dasar ===
pangkat = 2
masa_kerja = 15
tunjangan_per_tahun = 500_000

total_tunjangan = masa_kerja * tunjangan_per_tahun

print("=== Operasi Dasar ===")
print(f"Masa kerja          : {masa_kerja} tahun")
print(f"Tunjangan per tahun : Rp {tunjangan_per_tahun:,.0f}")
print(f"Total tunjangan     : Rp {total_tunjangan:,.0f}")
