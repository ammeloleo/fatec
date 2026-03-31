from abc import ABC, abstractmethod

class Dispositivo(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @abstractmethod
    def set_volume(self, volume):
        pass


class TV(Dispositivo):

    def __init__(self):
        self.volume = 10

    def ligar(self):
        print("TV ligada")

    def desligar(self):
        print("TV desligada")

    def set_volume(self, volume):
        self.volume = volume
        print(f"Volume da TV: {self.volume}")


class Radio(Dispositivo):

    def __init__(self):
        self.volume = 5

    def ligar(self):
        print("Rádio ligado")

    def desligar(self):
        print("Rádio desligado")

    def set_volume(self, volume):
        self.volume = volume
        print(f"Volume do Rádio: {self.volume}")


class ControleRemoto:

    def __init__(self, dispositivo):
        self.dispositivo = dispositivo

    def ligar(self):
        self.dispositivo.ligar()

    def desligar(self):
        self.dispositivo.desligar()


class ControleAvancado(ControleRemoto):

    def aumentar_volume(self):
        print("Aumentando volume...")
        self.dispositivo.set_volume(20)

    def diminuir_volume(self):
        print("Diminuindo volume...")
        self.dispositivo.set_volume(2)


if __name__ == "__main__":

    tv = TV()
    radio = Radio()

    controle_tv = ControleRemoto(tv)
    controle_radio = ControleAvancado(radio)

    print("\n--- Controle da TV ---")
    controle_tv.ligar()
    controle_tv.desligar()

    print("\n--- Controle do Rádio ---")
    controle_radio.ligar()
    controle_radio.aumentar_volume()
    controle_radio.diminuir_volume()
    controle_radio.desligar()