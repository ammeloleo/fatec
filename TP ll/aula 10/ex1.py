from abc import ABC, abstractmethod

# Interface comum
class Servico(ABC):
    @abstractmethod
    def operacao(self):
        pass


# Objeto real
class ServicoReal(Servico):
    def operacao(self):
        return "Operação realizada com sucesso!"


# Proxy
class ProxySeguranca(Servico):
    def __init__(self, usuario_autenticado):
        self.usuario_autenticado = usuario_autenticado
        self.servico_real = ServicoReal()

    def operacao(self):
        if self.usuario_autenticado:
            return self.servico_real.operacao()
        else:
            return "Acesso negado!"


# Uso
proxy1 = ProxySeguranca(True)
print(proxy1.operacao())

proxy2 = ProxySeguranca(False)
print(proxy2.operacao())