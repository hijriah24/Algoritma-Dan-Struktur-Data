# hijriah sisfo a
# File: variabel_statis_dinamis.py
# Deskripsi: Python hanya mendukung variabel dinamis. 
# Contoh berikut menunjukkan perilaku variabel yang dapat berubah tipe.

x = 10
print("x awal:", x, "(tipe:", type(x), ")")

x = "Sekarang string"
print("x berubah:", x, "(tipe:", type(x), ")")

# Contoh 'statis' buatan dengan konstanta (penamaan huruf besar)
PI = 3.14159  # dianggap tidak boleh diubah (konvensi, bukan aturan)
print("PI:", PI)
