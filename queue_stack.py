#declaration of stack
queue_size = 5
queue_dataset = [None] * queue_size
queue_head = -1
queue_tail = -1
status = True

#Check if the stack is full
def isFull():
    global queue_head, queue_tail, queue_size
    return queue_tail == queue_size - 1 

#Check if the stack is empty
def isEmpty():
    global queue_head, queue_tail
    return queue_head == -1 and queue_tail == -1

#adding data in dataset
def enQueue(queue_data):
    global queue_head, queue_tail, queue_dataset, queue_size
    if isFull():
        print('Stack Penuh')
    else:
        if isEmpty():
            queue_head = 0
            queue_tail = 0
        else:
            queue_tail += 1
        queue_dataset[queue_tail] = queue_data
        print(f'Data {queue_data} ditambahkan ke stack')
        print(f'Head: {queue_head}')
        print(f'Tail: {queue_tail}')
        print(queue_dataset)

#Remove one data in dataset
def deQueue():
    global queue_head, queue_tail, queue_dataset, queue_size
    if isEmpty():
        print('Stack Kosong')
    else:
        removed_data = queue_dataset[0]
        for i in range(queue_tail):
            queue_dataset[i] = queue_dataset[i + 1]
        queue_dataset[queue_tail] = None
        queue_tail -= 1
        if queue_tail < 0:
            queue_head = -1
            queue_tail = -1
        else:
            queue_head = (queue_head + 1) % queue_size
        print(f'Data yang dihapus adalah {removed_data}')
        print(f'Head: {queue_head}, Tail: {queue_tail}')
        print(queue_dataset)

#Wipe all data in dataset
def wipeQueue():
    global queue_head, queue_tail, queue_dataset, queue_size
    queue_dataset = [None] * queue_size
    queue_head = -1
    queue_tail = -1
    print('Data dalam stack sudah dihapus semua')
    print(queue_dataset)
    
    
#Main Program    
while status:
    print('===========================')
    print('Queue Stack Program')
    print('1. Input Data')
    print('2. Remove Data')
    print('3. Wipe Data')
    print('4. Exit')
    print('===========================')
    pilihan = int(input('Pilihan Anda : '))
    if pilihan == 1:
        data = input('Input data: ')
        enQueue(data)
    elif pilihan == 2:
        deQueue()
    elif pilihan == 3:
        wipeQueue()
    elif pilihan == 4:
        status = False
    else:
        print('Pilihan tidak valid. Program berhenti')
        break