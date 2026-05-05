# Subsistemas
class DVDPlayer:
    def ligar(self):
        print("DVD ligado")

    def reproduzir(self):
        print("Reproduzindo DVD")


class Projetor:
    def ligar(self):
        print("Projetor ligado")

    def ajustar_resolucao(self):
        print("Resolução ajustada")


class SistemaSom:
    def ligar(self):
        print("Som ligado")

    def ajustar_volume(self):
        print("Volume ajustado")


# Fachada
class HomeTheaterFacade:
    def __init__(self):
        self.dvd = DVDPlayer()
        self.projetor = Projetor()
        self.som = SistemaSom()

    def assistir_filme(self):
        print("Preparando para assistir filme...")
        self.dvd.ligar()
        self.projetor.ligar()
        self.projetor.ajustar_resolucao()
        self.som.ligar()
        self.som.ajustar_volume()
        self.dvd.reproduzir()


# Cliente
home_theater = HomeTheaterFacade()
home_theater.assistir_filme()