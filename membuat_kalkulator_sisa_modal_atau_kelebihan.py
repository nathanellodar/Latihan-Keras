print(10*"~", "WELCOME TO PROJEK KALKULATOR BELANJA BULANAN", 10*"~")
list_harga_belanja = []
modal = int(input("Masukan Uang Belanja Anda: Rp. "))

while True:
    print("1. Masukan Harga Belanja.")
    print("2. Menghitung Sisa Modal.")
    print("3. Tampilkan Harga-harga belanja.")
    print("4. Menghapus Salah Satu Harga Belanja.")
    print("5. Jika Sudah Selesai Menghitung.")
    pilihan = int(input("Masukan Pilihan anda:"))
    if pilihan == 1:
        harga = int(input("Masukan Jumlah Belanja: Rp. "))
        list_harga_belanja.append(harga)
    elif pilihan == 2:
        total_belanjaan = sum(list_harga_belanja)
        sisa = modal-total_belanjaan
        print("Sisa modal: Rp. ", sisa)
    elif pilihan == 3:
        print(list_harga_belanja)
    elif pilihan == 4:
        pilih_yang_mau_dihapus = int(input("Masukan, Harga yang mau dihapus: Rp. "))
        list_harga_belanja.remove(pilih_yang_mau_dihapus)
    elif pilihan == 5:
        print("LEBIH HEMAT LAGIIII")
        break
    else:
        print("PILIH YANG BENERR!!")
