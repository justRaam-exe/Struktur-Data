import random

class CircuQRandom:
    def __init__(self, qcapacity):
        self.CqueueR = [None] * qcapacity
        self.qcapacity = qcapacity
        self.qfront = -1
        self.qrear = -1
        self.first_insert_random = True  # Untuk kontrol pengisian acak hanya di awal

    def is_full(self):
        return (self.qrear + 1) % self.qcapacity == self.qfront

    def is_empty(self):
        return self.qfront == -1

    def enqueue(self, value):
        if self.is_full():
            print("Queue penuh! Tidak bisa menambahkan:", value)
            return

        if self.first_insert_random:
            rand_pos = random.randint(0, self.qcapacity - 1)
            self.qfront = rand_pos
            self.qrear = rand_pos
            self.CqueueR[rand_pos] = value
            self.first_insert_random = False
            print(f"{value} ditambahkan secara acak di index {rand_pos}.")
        else:
            self.qrear = (self.qrear + 1) % self.qcapacity
            self.CqueueR[self.qrear] = value
            print(f"{value} ditambahkan ke dalam queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue kosong!")
            return
        removed_value = self.CqueueR[self.qfront]
        if self.qfront == self.qrear:
            self.qfront = -1
            self.qrear = -1
            self.first_insert_random = True  # Reset agar next insert random lagi
        else:
            self.qfront = (self.qfront + 1) % self.qcapacity
        print(f"{removed_value} dihapus dari queue.")

    def display(self):
        # Tampilkan isi array queue
        for item in self.CqueueR:
            print(f"[{item}]", end=" ")
        print()  # baris baru

        # Tampilkan penanda posisi FRONT dan REAR
        for i in range(self.qcapacity):
            if i == self.qfront and i == self.qrear and not self.is_empty():
                print("  FR/R ", end="")  # front dan rear di tempat yang sama
            elif i == self.qfront:
                print(" FRONT ", end="")
            elif i == self.qrear:
                print("  REAR ", end="")
            else:
                print("       ", end="")
        print("\n")


def main():
    ukuran = int(input("Masukkan kapasitas queue: "))
    cq = CircuQRandom(ukuran)

    while True:
        print("===========================")
        print("Circular Queue Program")
        print("1. Enqueue data")
        print("2. Dequeue")
        print("3. Tampilkan isi queue")
        print("4. Keluar")
        print("===========================")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            if cq.is_full():
                print("Queue sudah penuh!")
            else:
                data = input("Masukkan data: ")
                cq.enqueue(data)
        elif pilihan == '2':
            cq.dequeue()
        elif pilihan == '3':
            cq.display()
        elif pilihan == '4':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
