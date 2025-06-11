class mahasigma:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.alamat1 = None
        self.alamat2 = None
        
data_mahasigma = [
    {"Nama": "Maki Oze", "Nim": "486910"},
    {"Nama": "Haumea", "Nim": "486911"},
    {"Nama": "Arthur Boyle", "Nim": "486912"}
]

nodes_mahasigma = [mahasigma(data["Nama"], data["Nim"]) for data in data_mahasigma]

nodes_mahasigma[0].alamat1 = nodes_mahasigma[1]
nodes_mahasigma[0].alamat2 = nodes_mahasigma[2]

def traverse_mahasigma(node):
    if node is None:
        return
    print("Nama:", node.nama)
    print("Nim:", node.nim)
    print()
    traverse_mahasigma(node.alamat1)
    traverse_mahasigma(node.alamat2)
    
traverse_mahasigma(nodes_mahasigma[0])        