#item perpustakaan

from abc import ABC, abstractmethod

class ItemPerpustakaan(ABC):
    def __init__ (self, judul, id_item):
        self.__judul = judul
        self.id_item = id_item

    @abstractmethod
    def deskripsi(self):
        pass

    def getID(self):
       return self.id_item
    
    def getJudul(self,judul):
       return self.__judul