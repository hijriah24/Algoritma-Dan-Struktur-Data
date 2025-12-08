# hijriah sisfo a
# File: insertion_sort.py
# Deskripsi: Implementasi algoritma Insertion Sort.

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # Geser elemen yang lebih besar ke kanan
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        
        data[j + 1] = key
    return data


# Contoh penggunaan
if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]
    print("Sebelum sorting:", data)

    hasil = insertion_sort(data)
    print("Sesudah sorting:", hasil)
