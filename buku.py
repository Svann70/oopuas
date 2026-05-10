from item import ItemPerpustakaan, Penulis

class Buku(ItemPerpustakaan):
    def __init__(self, penulis: Penulis, judul, id_item):
        self.penulis = penulis
        super().__init__(judul, id_item)

    def deskripsi(self):
        print(f"ID Item: {self.getID()}, Judul: {self.getJudul()}, Penulis: {self.penulis}, Kewarganegaraan: {self.penulis.kewarganegaraan}")