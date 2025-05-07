class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        
    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front
    
    def is_empty(self):
        return self.front == -1
    
    def display(self):
        if self.is_empty():
            print("Stack Kosong")
            return
        index = self.front
        print(f'Data dalam stack adalah: {self.queue}')
        while True:
            print(self.queue[index], end=' ')
            if index == self.rear:
                break
            index = (index + 1) % self.capacity
        print()
    
    def enqueue(self, value):
        if self.is_full():
            print("Stack Penuh")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        print(f"Data ditambahkan ke stack adalah {value}")
        
    def dequeue(self):
        if self.is_empty():
            print("Stack Kosong")
            return
        removed_value = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        print(f"Data yang dihapus adalah {removed_value}")

def main():
    Stuck_size = int(input('Masukan kapasitas stack: '))
    cq = CircularQueue(Stuck_size)
    
    while True:
        print('===========================')
        print('Circular Queue Program')
        print('1. Input data')
        print('2. Remove data')
        print('3. Display data')
        print('4. Exit')
        
        choice = int(input('Pilih menu: '))
        
        if choice == 1:
            value = input('Masukan data: ')
            cq.enqueue(value)
        elif choice == 2:
            cq.dequeue()
        elif choice == 3:
            cq.display()
        elif choice == 4:
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
                  
if __name__ == "__main__":
    main()