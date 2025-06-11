size_queue = 5
dataset_queue = [None] * size_queue
head_queue = -1
tail_queue = -1
status = True

def queueFull():
    global head_queue, tail_queue, size_queue
    return tail_queue == size_queue - 1

def queueEmpty():
    global head_queue, tail_queue
    return head_queue == -1 and tail_queue == -1

def enqueue_data(inputQueue_data):
    global size_queue, head_queue, tail_queue, dataset_queue
    inputQueue_data = int(inputQueue_data)  # Pastikan data berupa integer
    if queueFull():
        print('Stack Penuh')
    else:
        if queueEmpty():
            head_queue = 0
            tail_queue = 0
            dataset_queue[tail_queue] = inputQueue_data
        else:
            position_data = tail_queue
            # Geser elemen-elemen yang lebih besar ke kanan
            while position_data >= 0 and dataset_queue[position_data] > inputQueue_data:
                dataset_queue[position_data + 1] = dataset_queue[position_data]
                position_data -= 1
            # Masukkan data baru ke posisi yang sesuai
            dataset_queue[position_data + 1] = inputQueue_data
            tail_queue += 1
        print(f'Data {inputQueue_data} ditambahkan ke stack')
        print(dataset_queue)
        
def dequeue_data():
    global head_queue, tail_queue, dataset_queue, size_queue
    if queueEmpty():
        print('Stack Kosong')
    else:
        removed_data = dataset_queue[0]
        for i in range(tail_queue):
            dataset_queue[i] = dataset_queue[i + 1]
        dataset_queue[tail_queue] = None
        tail_queue -= 1
        if tail_queue < 0:
            head_queue = -1
            tail_queue = -1
        else:
            head_queue = (head_queue + 1) % size_queue
        print(f'Data yang dihapus adalah {removed_data}')
        print(dataset_queue)
        
def wipequeue_data():
    global head_queue, tail_queue, dataset_queue, size_queue
    dataset_queue = [None] * size_queue
    head_queue = -1
    tail_queue = -1
    print('Semua data sudah dihapus')
    print(dataset_queue)
    
while status:
    print('========================')
    print('Soal UTS Struktur Data')
    print('1. enqueue')
    print('2. dequeue')
    print('3. wipe dataset')
    print('4. exit')
    print('========================')
    choice_data = int(input('ur choice: '))
    if choice_data == 1:
        urData = input('input data: ')
        enqueue_data(urData)
    elif choice_data == 2:
        dequeue_data()
    elif choice_data == 3:
        wipequeue_data()
    elif choice_data == 4:
        status = False
        print('Thank you for using this program ^_^')
    else:
        print('Invalid Input. program stopped')
        print('Thank You ^_^')
        break        