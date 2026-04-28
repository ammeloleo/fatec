# Classe do serviço
class ServicoReal:
    def acessar(self):
        return "Acesso permitido ao serviço!"


# Classe do Proxy
class ProxyServico:
    def __init__(self):
        self.servico = ServicoReal()
        self.tentativas = 0
        self.limite = 3

    def acessar(self):
        # Verifica se o limite foi atingido
        if self.tentativas >= self.limite:
            return "Acesso bloqueado! Limite de tentativas excedido."

        # Conta a tentativa de acesso
        self.tentativas += 1

        return f"Tentativa {self.tentativas}: {self.servico.acessar()}"


# Testando o Proxy
proxy = ProxyServico()

print(proxy.acessar())  # 1ª tentativa
print(proxy.acessar())  # 2ª tentativa
print(proxy.acessar())  # 3ª tentativa
print(proxy.acessar())  # Bloqueado