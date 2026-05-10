from buku import Buku
from item import Penulis

class ManajerPerpustakaan:
    def __init__ (self):
        self.koleksi = []
        self.teurut =  False 
    
    def validasi_id_unik(self, id_baru):
        for buku in self.koleksi:
            if buku.getID() == id_baru:
               return False
        return True

    def tambah_buku(self):
        print("=== TAMBAH BUKU BARU ===")

        try:
            id_baru = int(input("Masukkan ID Buku: "))

            if not self.validasi_id_unik(id_baru):
                print('ID SUDAH DIGUNAKAN!')
                return
            
            judul = (input('Masukkan Judul: '))
            nama_penulis = input("Masukkan Nama Penulis : ")
            negara = (input("Masukkan Kewarganegaraan Penulis : "))

            penulis = Penulis(nama_penulis, negara)
            buku = Buku(id_baru, judul, penulis)
            self.koleksi.append(buku)
            self.terurut = False

            print("Buku berhasil ditambahkan!")

        except ValueError:
            print("Input ID harus berupa angka!")

    def tampilkan_koleksi(self):
        print("=== DAFTAR KOLEKSI BUKU ===")
        print("ID  |    Informasi Buku")
        print("----------------------------")

        if len(self.koleksi) == 0:
            print("Belum ada buku.")
            return

        for buku in self.koleksi:
            print(buku.deskripsi())
    

    # bubble sort
    def urutkan_koleksi(self):
        n = len(self.koleksi)

        for i in range(n):
            for j in range(0, n - i - 1):
                if self.koleksi[j].get_id() > self.koleksi[j + 1].get_id():

                    # gantian
                    self.koleksi[j], self.koleksi[j + 1] = (
                        self.koleksi[j + 1],
                        self.koleksi[j]
                    )

        self.terurut = True
        print("Koleksi buku berhasil diurutkan berdasarkan ID.")
    
    #Binary Search
    def cari_buku(self, id_target):

        if not self.terurut:
            print("Data belum terurut.")
            print("Sistem akan melakukan sorting terlebih dahulu...")
            self.urutkan_koleksi()

        kiri = 0
        kanan = len(self.koleksi) - 1

        while kiri <= kanan:
            mid = (kiri + kanan) // 2

            if self.koleksi[mid].get_id() == id_target:
                print("=== BUKU DITEMUKAN ===")
                print(self.koleksi[mid].deskripsi())
                return

            elif self.koleksi[mid].get_id() < id_target:
                kiri = mid + 1

            else:
                kanan = mid - 1

        print("Buku tidak ditemukan.")




