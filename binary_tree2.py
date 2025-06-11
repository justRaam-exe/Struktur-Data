class mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
        self.alamat1 = None
        self.alamat2 = None
        
mahasiswa_data1 = mahasiswa("Decade", "1357910")
mahasiswa_data2 = mahasiswa("Fourze", "1357911")
mahasiswa_data3 = mahasiswa("Agito", "1357912")

mahasiswa_data1.alamat1 = mahasiswa_data2
mahasiswa_data1.alamat2 = mahasiswa_data3

def traverse_dataMahasiswa(node):
    if node is None:
        return
    print("Nama:", node.nama)
    print("NPM:", node.npm)
    print()
    traverse_dataMahasiswa(node.alamat1)
    traverse_dataMahasiswa(node.alamat2)
    
traverse_dataMahasiswa(mahasiswa_data1)      