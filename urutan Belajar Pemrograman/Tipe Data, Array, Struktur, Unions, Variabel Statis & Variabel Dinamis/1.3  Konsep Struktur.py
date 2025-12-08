# hijriah sisfo a
# File: struktur.py
# Deskripsi: Konsep struktur menggunakan class Python (pengganti struct pada C).

class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

# Contoh penggunaan
mhs = Mahasiswa("Budi", "123456", "Informatika")
print("Nama:", mhs.nama)
print("NIM:", mhs.nim)
print("Jurusan:", mhs.jurusan)
