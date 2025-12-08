# hijriah sisfo a
# File: linear_search.py
# Deskripsi: Implementasi algoritma Linear Search (pencarian berurutan).

def linear_search(data, target):
    """
    Fungsi Linear Search
    Mengembalikan index dari nilai yang dicari jika ditemukan,
    dan -1 jika tidak ditemukan.
    """
    for i in range(data.size()):
        if data[i] == target:
            return i
    return -1

# Contoh penggunaan
if __name__ == "__main__":
    data = [5, 10, 15, 20, 25, 30]
    target = 20
    
    print("Data:", data)
    print("Mencari:", target)

    pos = linear_search(data, target)
    if pos != -1:
        print(f"Data ditemukan pada index {pos}")
    else:
        print("Data tidak ditemukan")
