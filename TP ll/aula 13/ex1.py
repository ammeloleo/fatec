# Flyweight
class Personagem:
    def __init__(self, tipo, arma):
        self.tipo = tipo
        self.arma = arma

    def exibir(self, x, y):
        print(f"{self.tipo} usando {self.arma} na posição ({x}, {y})")

# Factory
class FabricaPersonagem:
    personagens = {}

    @classmethod
    def obter_personagem(cls, tipo, arma):
        chave = (tipo, arma)

        if chave not in cls.personagens:
            cls.personagens[chave] = Personagem(tipo, arma)
            print("Novo personagem criado.")

        return cls.personagens[chave]

# Cliente
p1 = FabricaPersonagem.obter_personagem(
    "Guerreiro", "Espada"
)

p2 = FabricaPersonagem.obter_personagem(
    "Guerreiro", "Espada"
)

p3 = FabricaPersonagem.obter_personagem(
    "Mago", "Cajado"
)

p1.exibir(10, 20)
p2.exibir(30, 40)
p3.exibir(50, 60)