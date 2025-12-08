# hijriah sisfo a
# File: unions.py
# Deskripsi: Contoh konsep union sederhana menggunakan satu variabel fleksibel.

class UnionLike:
    def __init__(self):
        self.value = None

u = UnionLike()
u.value = 10           # integer
print("Value sebagai integer:", u.value)

u.value = "Hello"      # string
print("Value sebagai string:", u.value)

u.value = 3.14         # float
print("Value sebagai float:", u.value)
