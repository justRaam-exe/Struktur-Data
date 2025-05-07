# Inisialisasi deque
size = 5
deque = [None] * size
front = -1
rear = -1

def is_full():
    return front + 1 == rear

def is_emptyFront():
    return front == -1

def is_emptyRear():
    return rear == size

def insert_front(value):
    global front, rear
    if is_full():
        print("Deque penuh")
    else:
        front += 1
        deque[front] = value
    print(deque)

def insert_rear(value):
    global rear, deque
    if is_full():
        print("Deque penuh")
    else:
        rear -= 1
        deque[rear] = value
    print(deque)

def delete_front():
    global front, rear
    if is_emptyFront():
        print("Deque kosong")
        return
    else:
        for i in range(front):
            deque[i] = deque[i + 1]
        deque[front] = None
        front -= 1 
    print(deque)

def delete_rear():
    global front, rear
    if is_emptyRear():
        print("Deque kosong")
        return
    else:
        for i in range(size - 1, rear, -1):
            deque[i] = deque[i - 1]
        deque[rear] = None
        rear += 1
    print(deque)


# Menu interaktif
while True:
    print("\n--- Menu Deque ---")
    print("1. Tambah dari depan")
    print("2. Tambah dari belakang")
    print("3. Hapus dari depan")
    print("4. Hapus dari belakang")
    print("5. Tampilkan deque")
    print("6. Keluar")

    pilihan = input("Pilih operasi (1-6): ")

    if pilihan == "1":
        val = input("Masukkan nilai: ")
        insert_front(val)
    elif pilihan == "2":
        val = input("Masukkan nilai: ")
        insert_rear(val)
    elif pilihan == "3":
        delete_front()
    elif pilihan == "4":
        delete_rear()
    elif pilihan == "5":
        print("Isi deque:", deque)
    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
