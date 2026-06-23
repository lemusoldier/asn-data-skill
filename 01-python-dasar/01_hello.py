#!/usr/bin/env python3
"""01 — Hello World & Cetak Data
Contoh paling dasar: mencetak data ke layar.
"""

# Cetak teks sederhana
print("=== Selamat Datang di Python untuk ASN ===")
print()

# Cetak data pegawai
nama = "Budi Santoso"
nip = "198501152010011004"
golongan = "III/c"

print(f"Nama      : {nama}")
print(f"NIP       : {nip}")
print(f"Golongan  : {golongan}")
print()

# Cetak banyak data sekaligus
print("Daftar Pegawai:")
print("-" * 40)
print(f"  1. {nama} — {golongan}")
print(f"  2. Siti Rahayu — IV/a")
print(f"  3. Ahmad Hidayat — III/b")
print("-" * 40)
print("Total: 3 orang")
