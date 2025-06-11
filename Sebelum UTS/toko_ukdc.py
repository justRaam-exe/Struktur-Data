inventory = []

print('''
Selamat Datang di Toko UKDC
Pilih angka 1 - 4, untuk meng-eksekusi program dibawah
1. Tambah Data
2. Tampil Data
3. Hapus Data
4. Keluar''')

add_mem = input('Masukan input angka yang di mau : ')
if add_mem == '1':
    input_add = input('Masukan Sebuah data berbentuk string : ')
    inventory.append(input_add)
    print('Data telah ditambahkan ke dalam inventory')
    print(inventory)
elif add_mem == '2':
    print(inventory)
elif add_mem == '3':
    print(inventory)
    inventory.pop(input('masukan index barang yang mau dihapus : '))
    print('Data sudah terhapus')
    slct = input('ingin melihat data setelah di hapus? (y/n) : ')
    if slct == 'y':
        print(inventory)
    elif slct == 'n':
        print('Ya Sudah :v')
elif add_mem == '4':
    print('Terima kasih sudah berbelanja di toko UKDC, mampir lagi ya ^_^')