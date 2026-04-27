from abc import ABC, abstractmethod

# Classe base para inicialização
class Pizza(ABC):

    @abstractmethod
    def custo(self):
        pass

    @abstractmethod
    def descricao(self):
        pass


# Pizza base
class PizzaC(Pizza):

    def custo(self):
        return 20.0

    def descricao(self):
        return "Pizza de Calabresa"


# Decorator base
class DecoratorPizza(Pizza):
    # Recebe um objeto pizza como parâmetro
    # Isso permite "envolver" a pizza original

    def __init__(self, pizza: Pizza):
        self._pizza = pizza

    def custo(self):
        return self._pizza.custo()

    def descricao(self):
        return self._pizza.descricao()


# Ingredientes adicionais sendo somados com o custo da pizza base
class Queijo(DecoratorPizza):

    def custo(self):
        return self._pizza.custo() + 5.0

    def descricao(self):
        return self._pizza.descricao() + " + Queijo"


class Bacon(DecoratorPizza):

    def custo(self):
        return self._pizza.custo() + 8.0

    def descricao(self):
        return self._pizza.descricao() + " + Bacon"


class BordaRecheada(DecoratorPizza):

    def custo(self):
        return self._pizza.custo() + 6.0

    def descricao(self):
        return self._pizza.descricao() + " + Borda Recheada"


# Terminal
#Retorna a descrição e o custo total da pizza com os ingredientes adicionais
pizza = PizzaC()

pizza = Queijo(pizza)
pizza = Bacon(pizza)
pizza = BordaRecheada(pizza)

print("Descrição:", pizza.descricao())
print("Custo Total: R$", pizza.custo())