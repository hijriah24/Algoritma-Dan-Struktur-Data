# hijriah sisfo a
# File: stack.py
# Deskripsi: Implementasi struktur data Stack (LIFO) menggunakan list Python.
# Fitur: push, pop, peek, is_empty, size

class Stack:
    def __init__(self):
        self.items = []

    # Menambahkan item ke dalam stack (top)
    def push(self, item):
        self.items.append(item)
        print(f"Push: {item}")

    # Menghapus item dari stack (top)
    def pop(self):
        if self.is_empty():
            print("Pop gagal: Stack kosong!")
            return None
        removed = self.items.pop()
        print(f"Pop: {removed}")
        return removed

    # Melihat elemen paling atas stack tanpa menghapusnya
    def peek(self):
        if self.is_empty():
            print("Peek gagal: Stack kosong!")
            return None
        print(f"Peek: {self.items[-1]}")
        return self.items[-1]

    # Mengecek apakah stack kosong
    def is_empty(self):
        return len(self.items) == 0

    # Mendapatkan ukuran stack
    def size(self):
        return len(self.items)


# Contoh penggunaan Stack
if __name__ == "__main__":
    stack = Stack()

    # Push item
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Peek item paling atas
    stack.peek()

    # Pop item
    stack.pop()
    stack.pop()

    # Cek ukuran stack
    print("Ukuran stack sekarang:", stack.size())

    # Pop terakhir
    stack.pop()

    # Coba pop saat stack kosong
    stack.pop()
