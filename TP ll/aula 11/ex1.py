from abc import ABC, abstractmethod

# componente
class Item(ABC):
    @abstractmethod
    def mostrar(self, nivel=0):
        pass

# folha
class Arquivo(Item):
    def __init__(self, nome):
        self.nome = nome

    def mostrar(self, nome):
        print(" " * nivel+f"Arquivo: {self.nome}")

#composto
class Pasta(Item):
    def __init__(self, nome):
        self.nome = nome
        self.itens = []
    
    def adicionar(self, Item):
        self.itens.append(Item)

    def mostrar(self, nivel=0):
        print(" " * nivel + f"Pasta: {self.nome}")
        for Item in self.itens:
            item.mostrar(nivel + 1)

#uso
root = Pasta("root")
docs = Pasta("documentos")

docs.adicionar(Arquivo("cv.pdf"))
docs.adicionar(Arquivo("relatorio.docx"))

root.adicionar(docs)
root.adicionar(Arquivo("foto.png"))

root.mostrar()