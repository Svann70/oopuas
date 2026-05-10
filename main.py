from manajer import ManajerPerpustakaan

def main():
    manager = ManajerPerpustakaan()

    while True:
        print("\n=== MENU ===")
        print("1. Tampilkan Semua Koleksi")
        print("2. Tambah Buku Baru")
        print("3. Urutkan Koleksi")
        print("4. Cari Buku")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            manager.tampilkan_koleksi()

        elif pilihan == "2":
            manager.tambah_buku()

        elif pilihan == "3":
            manager.urutkan_koleksi()

        elif pilihan == "4":
            try:
                id_cari = int(input("Masukkan ID Buku: "))
                hasil = manager.cari_buku(id_cari)

                if hasil:
                    print(hasil.deskripsi())
    
            except ValueError:
                print("ID harus angka.")

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Menu tidak valid.")


if __name__ == "__main__":
    main()