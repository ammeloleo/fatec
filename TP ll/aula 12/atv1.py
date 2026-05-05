# Facade - Atividade 1

# Implemente  um facade para um sistema bancario com:
# conta(saldo)
#emrpestimo
#segurança(autenticação)

#  fachada deve ter um metodo realizar_transacao()

# Conta
class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}")
            return True
        else:
            print("Saldo insuficiente.")
            return False

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Saldo atual: R${self.saldo}")


# Subsistema: Empréstimo
class Emprestimo:
    def solicitar(self, valor):
        print(f"Empréstimo de R${valor} aprovado!")


# Subsistema: Segurança
class Seguranca:
    def autenticar(self, senha):
        if senha == "1234":
            print("Autenticação bem-sucedida.")
            return True
        else:
            print("Falha na autenticação.")
            return False

# Facade
class BancoFacade:
    def __init__(self, saldo_inicial):
        self.conta = Conta(saldo_inicial)
        self.emprestimo = Emprestimo()
        self.seguranca = Seguranca()

    def realizar_transacao(self, tipo, valor, senha):
        print("\nIniciando transação...")

        if not self.seguranca.autenticar(senha):
            print("Transação cancelada.")
            return

        if tipo == "saque":
            self.conta.sacar(valor)

        elif tipo == "deposito":
            self.conta.depositar(valor)

        elif tipo == "emprestimo":
            self.emprestimo.solicitar(valor)
            self.conta.depositar(valor)

        else:
            print("Tipo de transação inválido.")


# Cliente
banco = BancoFacade(1000)

banco.realizar_transacao("saque", 200, "1234")
banco.realizar_transacao("deposito", 300, "1234")
banco.realizar_transacao("emprestimo", 500, "1234")
banco.realizar_transacao("saque", 100, "0000")  # senha errada