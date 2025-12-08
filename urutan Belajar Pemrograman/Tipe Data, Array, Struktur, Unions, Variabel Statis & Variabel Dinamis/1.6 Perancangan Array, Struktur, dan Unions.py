# hijriah sisfo a
# File: array_struktur_unions.py
# Deskripsi: Perancangan gabungan array, struktur, dan union-like pada Python.

class Barang:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

# Array berisi struktur (class)
daftar_barang = [
    Barang("Buku", 12000),
    Barang("Pulpen", 3000),
    Barang("Penghapus", 2000)
]

print("Daftar Barang:")
for b in daftar_barang:
    print("-", b.nama, "=", b.harga)

# Contoh array yang berisi union-like
class UnionLike:
    def __init__(self):
        self.value = None

data_union = [UnionLike() for _ in range(3)]
data_union[0].value = 123
data_union[1].value = "Teks"
data_union[2].value = 9.99

print("\nIsi union-like array:")
for i, u in enumerate(data_union):
    print(f"Index {i}: {u.value} (tipe {type(u.value)})")
