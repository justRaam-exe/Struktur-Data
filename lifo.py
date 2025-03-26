size = 3
dataset = []
top = -1
status = True

def push(data):
    global top, dataset
    if top == size - 1:
        print('Stack Penuh')
    else:
        dataset.append(data)
        top += 1

def pop():
    global top, dataset
    if top == -1:
        print('Stack Kosong')
    else:
        removed_data = dataset[top]
        del dataset[top]
        top -= 1

def clear():
    global top, dataset
    if top == -1:
        print('Stack Kosong')
    else:
        for _ in range(top + 1):
            pop()
            
def peek():
    global top, dataset
    if top == -1:
        print('Stack Kosong')
    else:
        print('Top data is ' + dataset[top])

while status:
    print('===========================')
    print('Dataset: ' + str(dataset))
    print('1. Input Data')
    print('2. Hapus Data')
    print('3. Clear Data')
    print('4. Lihat Data Top')
    print('5. Exit')
    print('===========================')
    pilihan = int(input('Pilihan Anda : '))
    if pilihan == 1:
        a = input('Input data: ')
        push(a)
    elif pilihan == 2:
        pop()
    elif pilihan == 3:
        clear()
    elif pilihan == 4:
        peek()
    elif pilihan == 5:
        break