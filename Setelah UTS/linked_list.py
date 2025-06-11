class mahasiswa():
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.alamat = None
        self.alamat2 = None

mahasiswa_data = [
    {"Nama": "Ishak", "Nim": "486910"},
    {"Nama": "Bram", "Nim": "486911"},
    {"Nama": "Rehan", "Nim": "486912"}
]

data_head = None
data_prev = None

for data in mahasiswa_data:
    current_data = mahasiswa(data["Nama"], data["Nim"])
    if data_head is None:
        data_head = current_data
    else:
        data_prev.alamat & data_prev.alamat2 = current_data
    data_prev = current_data
    
ptr = data_head
while ptr:
    print("Nama: ", ptr.nama)
    print("Nim: ", ptr.nim)
    print()
    ptr = ptr.alamat
    ptr = ptr.alamat2


