from item import ItemPerpustakaan, Penulis

class Buku(ItemPerpustakaan):
    def __init__(self, id_item, judul, penulis: Penulis):
        self.penulis = penulis
        super().__init__(id_item, judul)

    def deskripsi(self):
        return (f"[{self.getID()}   ] Buku: {self.getJudul()}  |  {self.penulis.nama}({self.penulis.kewarganegaraan})")