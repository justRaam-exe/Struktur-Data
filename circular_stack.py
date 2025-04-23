# # Circular Stack implementation
class CircularStack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1
        self.coun = 0
        
    def full_data(self):
        return self.coun == self.size
    
    def empty_data(self):
        return self.coun == 0
        
    def push_data(self, value):
        if self.full_data():
            print('Stack Penuh lee')
            return
        self.top = (self.top + 1) % self.size
        self.stack[self.top] = value
        self.coun += 1
        print(f'Data ditambahkan ke stack adalah {value}')
                
    def pop_data(self):
        if self.empty_data():
            print('Stack Kosong nih')
            return
        pop_value = self.stack[self.top]
        self.stack[self.top] = None
        self.top = (self.top - 1 + self.size) % self.size
        self.coun -= 1
        print(f'Data yang dihapus adalah {pop_value}')
        return pop_value
    
    def display_data(self):
        print(f'Data dalam stack adalah: {self.stack}')
        
    def clear_data(self):
        if self.empty_data():
            print('Stack Kosong')
        else:
            for _ in range(self.coun):
                self.pop_data()
            print('Data dalam stack sudah dihapus semua')
            
    def display_top(self):
        if self.empty_data():
            print('Stack Kosong')
        else:
            print(f'Top stack adalah: {self.stack[self.top]}')

def main():
    size = int(input('Masukan kapasitas stack: '))
    Circu_stack = CircularStack(size)
    
    while True:
        print('===========================')
        print('Circular Stack Program')
        print('1. Input data')
        print('2. Remove data')
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
            Circu_stack.display_top()
        elif answer == '5':
            print('God Bless You, Thank You')
            break
            
if __name__ == '__main__':
    main()