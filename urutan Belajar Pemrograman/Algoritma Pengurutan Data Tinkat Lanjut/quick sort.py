# hijriah sisfo a
# File: quick_sort.py
# Deskripsi: Implementasi algoritma Quick Sort dengan metode Lomuto partition.

def quick_sort(data, low, high):
    if low < high:
        p = partition(data, low, high)
        quick_sort(data, low, p - 1)
        quick_sort(data, p + 1, high)
    return data


def partition(data, low, high):
    pivot = data[high]  # pivot terakhir
    i = low - 1

    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]

    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1


# Contoh penggunaan
if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("Sebelum sorting:", data)

    hasil = quick_sort(data, 0, len(data) - 1)
    print("Sesudah sorting:", hasil)
