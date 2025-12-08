# hijriah sisfo a
# File: shell_sort.py
# Deskripsi: Implementasi algoritma Shell Sort.

def shell_sort(data):
    gap = len(data) // 2

    while gap > 0:
        for i in range(gap, len(data)):
            temp = data[i]
            j = i

            # Insertion sort sesuai gap
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap

            data[j] = temp
        gap //= 2

    return data


# Contoh penggunaan
if __name__ == "__main__":
    data = [12, 34, 54, 2, 3]
    print("Sebelum sorting:", data)

    hasil = shell_sort(data)
    print("Sesudah sorting:", hasil)
