# Circular Stack With random
# import random

# class CircularStack:
#     def __init__(self, size):
#         self.size = size
#         self.stack = [None] * size
#         self.coun = 0

#     def full_data(self):
#         return self.coun == self.size

#     def empty_data(self):
#         return self.coun == 0

#     def push_data(self, value):
#         if self.full_data():
#             print('Stack Penuh lee')
#             return
        
#         # Cari semua index kosong
#         empty_indexes = [i for i, val in enumerate(self.stack) if val is None]
        
#         if not empty_indexes:
#             print('Tidak ada slot kosong.')
#             return
        
#         # Pilih salah satu index kosong secara acak
#         rand_index = random.choice(empty_indexes)
#         self.stack[rand_index] = value
#         self.coun += 1
#         print(f'Data "{value}" dimasukkan ke posisi acak: index {rand_index}')

#     def pop_data(self):
#         if self.empty_data():
#             print('Stack Kosong nih')
#             return

#         # Hapus elemen terakhir (berdasarkan urutan array)
#         for i in range(self.size - 1, -1, -1):
#             if self.stack[i] is not None:
#                 pop_value = self.stack[i]
#                 self.stack[i] = None
#                 self.coun -= 1
#                 print(f'Data yang dihapus adalah "{pop_value}" dari index {i}')
#                 return pop_value

#     def display_data(self):
#         print(f'Data dalam stack: {self.stack}')

#     def clear_data(self):
#         if self.empty_data():
#             print('Stack Kosong')
#         else:
#             for i in range(self.size):
#                 self.stack[i] = None
#             self.coun = 0
#             print('Data dalam stack sudah dihapus semua')

import random

class CircularStack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.coun = 0
        self.input_order = []  # Untuk menyimpan urutan index input

    def full_data(self):
        return self.coun == self.size

    def empty_data(self):
        return self.coun == 0

    def push_data(self, value):
        if self.full_data():
            print('Stack Penuh lee')
            return

        empty_indexes = [i for i, val in enumerate(self.stack) if val is None]

        if not empty_indexes:
            print('Tidak ada slot kosong.')
            return

        rand_index = random.choice(empty_indexes)
        self.stack[rand_index] = value
        self.input_order.append(rand_index)  # Simpan urutan input
        self.coun += 1
        print(f'Data "{value}" dimasukkan ke posisi acak: index {rand_index}')

    def pop_data(self):
        if self.empty_data():
            print('Stack Kosong nih')
            return

        last_index = self.input_order.pop()  # Ambil index terakhir yang diinput
        pop_value = self.stack[last_index]
        self.stack[last_index] = None
        self.coun -= 1
        print(f'Data yang dihapus adalah "{pop_value}" dari index {last_index}')
        return pop_value

    def display_data(self):
        if self.empty_data():
            print(f'Data dalam stack: {self.stack}')
            print('Stack kosong')
            return

        print(f'Data dalam array fisik: {self.stack}')
        print('\nVisualisasi urutan (paling baru → paling lama):')
        
        # Tampilkan urutan input terbaru di kiri
        for idx in reversed(self.input_order):
            print(f'| {self.stack[idx]} |', end=' ')
        print('\n' + '-' * 30)

           

    def clear_data(self):
        if self.empty_data():
            print('Stack Kosong')
        else:
            for i in self.input_order:
                self.stack[i] = None
            self.input_order.clear()
            self.coun = 0
            print('Data dalam stack sudah dihapus semua')


def main():
    size = int(input('Masukan kapasitas stack: '))
    Circu_stack = CircularStack(size)

    while True:
        print('===========================')
        print('Circular Stack Program')
        print('1. Input data (acak)')
        print('2. Remove data (dari akhir)')
        print('3. Clear data')
        print('4. Display data')
        print('5. Exit program')
        print('===========================')

        answer = input('Choose your answer: ')
        if answer == '1':
            input_data = input('Input data: ')
            Circu_stack.push_data(input_data)
        elif answer == '2':
            Circu_stack.pop_data()
        elif answer == '3':
            Circu_stack.clear_data()
        elif answer == '4':
            Circu_stack.display_data()
        elif answer == '5':
            print('God Bless You, Thank You')
            break

if __name__ == '__main__':
    main()
