# Perbedaan List dan Tuple dalam Python

# 1. Sintaks Pembuatan
# List menggunakan kurung siku []
list_buah = ["apel", "pisang", "mangga"]

# Tuple menggunakan kurung biasa ()
tuple_buah = ("apel", "pisang", "mangga")

print(f"Ini adalah List: {list_buah}, tipe: {type(list_buah)}")
print(f"Ini adalah Tuple: {tuple_buah}, tipe: {type(tuple_buah)}")
print("-" * 30)


# 2. Sifat Mutable (List) vs Immutable (Tuple)

# --- LIST (Mutable) ---
# Kita bisa mengubah, menambah, atau menghapus elemen dari list.
print("Mencoba mengubah elemen pada LIST...")
print(f"List sebelum diubah: {list_buah}")

# Mengubah elemen pada indeks ke-1
list_buah[1] = "jeruk"
print(f"List setelah diubah: {list_buah}")

# Menambah elemen baru
list_buah.append("durian")
print(f"List setelah ditambah elemen: {list_buah}")
print("-" * 30)


# --- TUPLE (Immutable) ---
# Kita TIDAK BISA mengubah elemen dari tuple.
# Mencoba mengubah elemen pada tuple akan menghasilkan TypeError.
print("Mencoba mengubah elemen pada TUPLE...")
print(f"Tuple sebelum diubah: {tuple_buah}")

try:
    # Baris kode ini akan menyebabkan error
    tuple_buah[1] = "jeruk"
    print(f"Tuple setelah diubah: {tuple_buah}")
except TypeError as e:
    print(f"Error terjadi! -> {e}")
    print("Ini membuktikan bahwa tuple bersifat immutable (tidak dapat diubah).")
print("-" * 30)

# 3. Perbedaan Metode
print("Perbedaan Metode:")
print(f"Metode List: {sorted([m for m in dir(list) if not m.startswith('__')])}")
print(f"Metode Tuple: {sorted([m for m in dir(tuple) if not m.startswith('__')])}")
