# create a variable
size = 6
datasetZ = [None] * size
top1 = -1
top2 = size
status = True

# function to peek data in top 1
def peek1(data):
    global top1, datasetZ
    if top1 == -1:
        print('Stack 1 Kosong')
    else:
        print('Top data stack 1 is ' + datasetZ[top1])

# function to peek data in top 2        
def peek2(data):
    global top2, datasetZ
    if top2 == size:
        print('Stack 2 Kosong')
    else:
        print('Top data stack 2 is ' + datasetZ[top2])

# function to add data in stack 1        
def push1(data):
    global top1, top2, datasetZ
    if top2 - top1 > 1:
        datasetZ[top1 + 1] = data
        top1 += 1
        peek1(data)
    else:
        print('Stack 1 Penuh')

# function to add data in stack 2
def push2(data):
    global top1, top2, datasetZ
    if top2 - top1 > 1:
        datasetZ[top2 - 1] = data
        top2 -= 1
        peek2(data)
    else:
        print('Stack 2 Penuh')

# function to remove data stack 1
def pop1(data):
    global top1, datasetZ
    if top1 == -1:
        print('Stack 1 Kosong')
    else:
        hapus_data = datasetZ[top1]
        datasetZ[top1] = None
        top1 -= 1
        print('Data yang dihapus adalah ' + '[' + hapus_data + ']')
        
# function to remove data stack 2
def pop2(data):
    global top1, top2, datasetZ
    if top2 == size:
        print('Stack 2 Kosong')
    else:
        hapus_data = datasetZ[top2]
        datasetZ[top2] = None
        top2 += 1
        print('Data yang dihapus adalah ' + hapus_data)
        
# function to clear data stack 1
def clear1(data):
    global top1, datasetZ
    if top1 == -1:
        print('Stack 1 Kosong')
    else:
        for _ in range(top1 + 1):
            pop1(data)

# function to clear data stack 2
def clear2(data):
    global top2, datasetZ
    if top2 == size:
        print('Stack 2 Kosong')
    else:
        for _ in range(size - top2):
            pop2(data)
            
# function to clear all data in both stacks
def clear_data(data):
    global top1, top2, datasetZ
    if top1 == -1 and top2 == size:
        print('Stack Kosong')
    else:
        for _ in range(top1 + 1):
            pop1(data)
        for _ in range(size - top2):
            pop2(data)
            
    
# Main looping program 
while status == True:        
    print('''
Double Stack Program
choose:
1. Push data 1
2. Push data 2
3. Pop data 1
4. Pop data 2
5. Clear data 1
6. Clear data 2
7. Clear data
8. Look at dataset''')
    ur_ans = input('Your Answer: ')
    if ur_ans == '1':
        data = input('Input data: ')
        push1(data)
    elif ur_ans == '2':
        data = input('Input data: ')
        push2(data)
    elif ur_ans == '3':
        pop1(data)
    elif ur_ans == '4':
        pop2(data)
    elif ur_ans == '5':
        clear1(data)
    elif ur_ans == '6':
        clear2(data)
    elif ur_ans == '7':
        clear_data(data)
    elif ur_ans == '8':
        print('Dataset: ' + str(datasetZ))
    else:
        print('Input salah')
        break