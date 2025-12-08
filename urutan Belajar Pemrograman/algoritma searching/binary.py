
# hijriah sisfo a
# File: binary_search.py
# Deskripsi: Implementasi algoritma Binary Search (pencarian biner).
# Catatan: Binary Search HANYA bekerja pada data yang sudah terurut.

def binary_search(data, target):
    """
    Fungsi Binary Search
    Mengembalikan index dari nilai yang dicari jika ditemukan,
    dan -1 jika tidak ditemukan.
    """
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == target:
            return mid
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

# Contoh penggunaan
if __name__ == "__main__":
    data = [5, 10, 15, 20, 25, 30]
    target = 25

    print("Data:", data)
    print("Mencari:", target)

    pos = binary_search(data, target)
    if pos != -1:
        print(f"Data ditemukan pada index {pos}")
    else:
        print("Data tidak ditemukan")
