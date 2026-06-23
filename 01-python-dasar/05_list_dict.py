#!/usr/bin/env python3
"""05 — List & Dictionary
Struktur data paling umum untuk mengelola data ASN.
"""

# === LIST: Kumpulan Data ===
print("=== List Sederhana ===")
daftar_nama = ["Budi Santoso", "Siti Rahayu", "Ahmad Hidayat"]
print(f"Jumlah: {len(daftar_nama)} orang")
print(f"Pertama: {daftar_nama[0]}")
print(f"Terakhir: {daftar_nama[-1]}")

daftar_nama.append("Dewi Lestari")  # tambah data
print(f"Setelah ditambah: {daftar_nama}")
print()

# === DICTIONARY: Data Key-Value ===
print("=== Dictionary ===")
pegawai = {
    "nama": "Budi Santoso",
    "nip": "198501152010011004",
    "golongan": "III/c",
    "jabatan": "Analis Kepegawaian",
    "unit": "Subbag Kepegawaian",
    "gaji_pokok": 5_500_000,
    "tunjangan": 1_200_000,
}

for key, value in pegawai.items():
    print(f"  {key:<15}: {value}")
print()

# === LIST OF DICTIONARIES: Format Umum Data ASN ===
print("=== Daftar Pegawai Lengkap ===")
data_pegawai = [
    {
        "nama": "Budi Santoso",
        "nip": "198501152010011004",
        "golongan": "III/c",
        "jabatan": "Analis Kepegawaian",
        "gaji_pokok": 5_500_000,
    },
    {
        "nama": "Siti Rahayu",
        "nip": "198803122012012003",
        "golongan": "IV/a",
        "jabatan": "Kepala Subbag",
        "gaji_pokok": 6_200_000,
    },
    {
        "nama": "Ahmad Hidayat",
        "nip": "199006012015011001",
        "golongan": "III/b",
        "jabatan": "Staff Umum",
        "gaji_pokok": 5_000_000,
    },
]

for i, p in enumerate(data_pegawai, 1):
    print(f"{i}. {p['nama']}")
    print(f"   NIP      : {p['nip']}")
    print(f"   Golongan : {p['golongan']}")
    print(f"   Jabatan  : {p['jabatan']}")
    print(f"   Gaji     : Rp {p['gaji_pokok']:,.0f}")
    print()

# === MENYIMPAN & MENGAKSES ===
print("=== Akses Spesifik ===")
# Ambil semua gaji
total = sum(p["gaji_pokok"] for p in data_pegawai)
print(f"Total gaji seluruh pegawai: Rp {total:,.0f}")

# Cari pegawai tertentu
nama_dicari = "Siti Rahayu"
hasil = [p for p in data_pegawai if p["nama"] == nama_dicari]
if hasil:
    print(f"Ditemukan: {hasil[0]['nama']} — {hasil[0]['jabatan']}")
