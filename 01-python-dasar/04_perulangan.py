#!/usr/bin/env python3
"""04 — Perulangan (Loop)
Contoh: memroses daftar data ASN secara berulang.
"""

# === Loop dengan for ===
pegawai = [
    {"nama": "Budi Santoso", "nip": "198501152010011004", "gol": "III/c", "gaji": 5_500_000},
    {"nama": "Siti Rahayu", "nip": "198803122012012003", "gol": "IV/a", "gaji": 6_200_000},
    {"nama": "Ahmad Hidayat", "nip": "199006012015011001", "gol": "III/b", "gaji": 5_000_000},
    {"nama": "Dewi Lestari", "nip": "199201252018012005", "gol": "III/a", "gaji": 4_500_000},
]

print("=" * 65)
print(f"{'NO':<4} {'NAMA':<20} {'NIP':<22} {'GOL':<6} {'GAJI':>12}")
print("=" * 65)

total_gaji = 0
for i, p in enumerate(pegawai, 1):
    print(f"{i:<4} {p['nama']:<20} {p['nip']:<22} {p['gol']:<6} Rp {p['gaji']:>10,}")
    total_gaji += p["gaji"]

print("-" * 65)
print(f"{'TOTAL':>50} Rp {total_gaji:>10,}")
print(f"{'RATA-RATA':>50} Rp {total_gaji // len(pegawai):>10,}")
print("=" * 65)
print()

# === Loop dengan range ===
print("=== Contoh: Cetak Nomer Urut SKP ===")
for i in range(1, 6):
    print(f"  SKP-{i:03d} — Penilaian ke-{i}")

print()

# === List comprehension ===
# Mengambil semua nama dari list dictionary
nama_list = [p["nama"] for p in pegawai]
print(f"Daftar nama: {', '.join(nama_list)}")

# Filter: pegawai golongan III ke atas
gol_tinggi = [p["nama"] for p in pegawai if p["gol"].startswith("III") or p["gol"].startswith("IV")]
print(f"Gol III+: {', '.join(gol_tinggi)}")
