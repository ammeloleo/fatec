from abc import ABC, abstractmethod

# Classe abstrata base
class Bebida(ABC):

    @abstractmethod
    def custo(self):
        pass

    @abstractmethod
    def descricao(self):
        pass


# Implementação concreta
class CafeSimples(Bebida):

    def custo(self):
        return 5.0

    def descricao(self):
        return "Café Simples"


# Classe Decoradora
class DecoradorBebida(Bebida):

    def __init__(self, bebida: Bebida):
        self._bebida = bebida

    def custo(self):
        return self._bebida.custo()

    def descricao(self):
        return self._bebida.descricao()


# Decorador Leite
class Leite(DecoradorBebida):

    def custo(self):
        return self._bebida.custo() + 2.0

    def descricao(self):
        return self._bebida.descricao() + ", leite"


# Decorador Chocolate
class Chocolate(DecoradorBebida):

    def custo(self):
        return self._bebida.custo() + 3.0

    def descricao(self):
        return self._bebida.descricao() + ", chocolate"


# Uso
bebida = CafeSimples()
bebida = Leite(bebida)
bebida = Chocolate(bebida)

print("Descrição:", bebida.descricao())
print("Custo R$:", bebida.custo())