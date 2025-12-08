# hijriah sisfo a
# File: merge_sort.py
# Deskripsi: Implementasi algoritma Merge Sort (rekursif).

def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        # Rekursi
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Proses merging
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        # Tambah sisa elemen left
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        # Tambah sisa elemen right
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

    return data


# Contoh penggunaan
if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Sebelum sorting:", data)
    
    hasil = merge_sort(data)
    print("Sesudah sorting:", hasil)
