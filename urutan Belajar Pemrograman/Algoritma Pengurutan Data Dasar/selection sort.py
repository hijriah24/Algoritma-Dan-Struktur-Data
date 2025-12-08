# hijriah sisfo a
# File: selection_sort.py
# Deskripsi: Implementasi algoritma Selection Sort.

def selection_sort(data):
    n = len(data)
    for i in range(n):
        # Cari index elemen terkecil
        min_index = i
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        # Tukar posisi
        data[i], data[min_index] = data[min_index], data[i]
    return data


# Contoh penggunaan
if __name__ == "__main__":
    data = [29, 10, 14, 37, 14]
    print("Sebelum sorting:", data)

    hasil = selection_sort(data)
    print("Sesudah sorting:", hasil)
