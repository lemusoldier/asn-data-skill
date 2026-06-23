#!/usr/bin/env python3
"""03 — Percabangan (If/Else)
Contoh: menentukan tunjangan berdasarkan golongan.
"""

# === If/Else Sederhana ===
golongan = "III/c"

print(f"Golongan: {golongan}")
print()

if golongan.startswith("I"):
    tunjangan = 500_000
    level = "Juru Muda"
elif golongan.startswith("II"):
    tunjangan = 750_000
    level = "Pengatur"
elif golongan.startswith("III"):
    tunjangan = 1_000_000
    level = "Penata Muda"
elif golongan.startswith("IV"):
    tunjangan = 1_500_000
    level = "Pembina"
else:
    tunjangan = 0
    level = "Tidak Diketahui"

print(f"Level    : {level}")
print(f"Tunjangan: Rp {tunjangan:,.0f}/bulan")
print()

# === Percabangan dengan Input ===
print("--- Cek Kelayakan TPP ---")
skp = 85  # Nilai SKP (0-100)

if skp >= 90:
    status = "Sangat Baik"
    tpp = "100%"
elif skp >= 80:
    status = "Baik"
    tpp = "85%"
elif skp >= 70:
    status = "Cukup"
    tpp = "70%"
else:
    status = "Kurang"
    tpp = "50%"

print(f"Nilai SKP    : {skp}")
print(f"Penilaian    : {status}")
print(f"Persentase TPP: {tpp}")
