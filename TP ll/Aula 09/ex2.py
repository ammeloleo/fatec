from abc import ABC, abstractmethod


# Componente

class Notificador(ABC):

    @abstractmethod
    def enviar(self, mensagem):
        pass



# Componente Concreto

class NotificadorEmail(Notificador):

    def enviar(self, mensagem):
        return f"Enviando por Email: {mensagem}"



# Decorator Base

class DecoradorNotificador(Notificador):

    def __init__(self, notificador):
        self._notificador = notificador

    def enviar(self, mensagem):
        return self._notificador.enviar(mensagem)



# Decoradores Concretos

class NotificadorSMS(DecoradorNotificador):

    def enviar(self, mensagem):
        return self._notificador.enviar(mensagem) + \
               f"\nEnviado por SMS: {mensagem}"


class NotificadorWhatsapp(DecoradorNotificador):

    def enviar(self, mensagem):
        return self._notificador.enviar(mensagem) + \
               f"\nEnviado por WhatsApp: {mensagem}"



# Utilização

notificador = NotificadorEmail()
notificador = NotificadorSMS(notificador)
notificador = NotificadorWhatsapp(notificador)

print(notificador.enviar("Sistema em manutenção"))