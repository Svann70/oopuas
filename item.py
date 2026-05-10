#item perpustakaan

from abc import ABC, abstractmethod

class ItemPerpustakaan(ABC):
    def __init__ (self, id_item, judul):
        self.id_item = id_item
        self.__judul = judul

    @abstractmethod
    def deskripsi(self):
        pass

    def getID(self):
       return self.id_item
    
    def getJudul(self):
       return self.__judul
    
class Penulis:
    def __init__(self,nama,kewarganegaraan):
        self.nama = nama
        self.kewarganegaraan = kewarganegaraan
    
    def __str__(self):
        return f'{self.nama} ({self.kewarganegaraan})'
