# Classe State
class EstadoSemaforo:
    def mudar(self):
        pass


# Estado Verde
class Verde(EstadoSemaforo):

    def mudar(self):
        print("Verde -> Siga")
        return Amarelo()


# Estado Amarelo
class Amarelo(EstadoSemaforo):

    def mudar(self):
        print("Amarelo -> Atenção")
        return PiscandoAmarelo()


# Novo Estado: Piscando Amarelo
class PiscandoAmarelo(EstadoSemaforo):

    def mudar(self):
        print("Piscando Amarelo -> Atenção Redobrada")
        return Vermelho()


# Estado Vermelho
class Vermelho(EstadoSemaforo):

    def mudar(self):
        print("Vermelho -> Pare")
        return Verde()


# Context
class Semaforo:

    def __init__(self):
        self.estado = Verde()

    def proximo(self):
        self.estado = self.estado.mudar()


# Programa principal
semaforo = Semaforo()

for i in range(8):
    semaforo.proximo()