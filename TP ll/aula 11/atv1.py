from abc import ABC, abstractmethod

#----- Menu Restaurante -----

# Classe Base
class ItemMenu(ABC):
    @abstractmethod
    def get_preco(self):
        pass

#Folha: Prato
class Prato(ItemMenu):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def get_preco(self):
        return self.preco

#Composto: Combo
class Combo(ItemMenu):
    def __init__(self, nome):
        self.nome = nome
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def get_preco(self):
        total = 0
        for item in self.itens:
            total += item.get_preco()
        return total

#----- Uso -----

combo1 = Combo("Combo 1")
combo1.adicionar(Prato("Hamburguer", 10))
combo1.adicionar(Prato("Batata Frita", 5))

print("Preço do combo1:", combo1.get_preco())