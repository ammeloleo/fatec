from abc import ABC, abstractmethod

# =====================================================
# FACTORY METHOD
# =====================================================

# Classe abstrata de pagamento
class Pagamento(ABC):

    @abstractmethod
    def pagar(self, valor):
        pass

# Pagamento com cartão
class PagamentoCartao(Pagamento):

    def pagar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} realizado com CARTÃO.")

# Pagamento com PIX
class PagamentoPix(Pagamento):

    def pagar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} realizado com PIX.")

# NOVO MÉTODO: BOLETO
class PagamentoBoleto(Pagamento):

    def pagar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} realizado com BOLETO.")

# Factory Method
class FabricaPagamento:

    @staticmethod
    def criar_pagamento(tipo):

        if tipo == "cartao":
            return PagamentoCartao()

        elif tipo == "pix":
            return PagamentoPix()

        elif tipo == "boleto":
            return PagamentoBoleto()

        else:
            raise ValueError("Tipo de pagamento inválido.")
        
# =====================================================
# CHAIN OF RESPONSIBILITY
# =====================================================

# Classe base dos validadores
class Validador:

    def __init__(self):
        self.proximo = None

    def definir_proximo(self, proximo):
        self.proximo = proximo
        return proximo

    def processar(self, pedido):

        if self.proximo:
            return self.proximo.processar(pedido)

        return True
    
# Verifica estoque
class ValidarEstoque(Validador):

    def processar(self, pedido):

        if pedido["estoque"] <= 0:
            print("Produto sem estoque.")
            return False

        print("Estoque validado.")
        return super().processar(pedido)

# Verifica valor mínimo
class ValidarValorMinimo(Validador):

    def processar(self, pedido):

        if pedido["valor"] < 10:
            print("Pedido abaixo do valor mínimo.")
            return False

        print("Valor mínimo validado.")
        return super().processar(pedido)

# Verifica CPF
class ValidarCPF(Validador):

    def processar(self, pedido):

        cpf = pedido["cpf"]

        # Remove caracteres não numéricos
        cpf = ''.join(filter(str.isdigit, cpf))

        # CPF precisa ter 11 dígitos
        if len(cpf) != 11:
            print("CPF inválido.")
            return False

        # Não permite todos os números iguais
        if cpf == cpf[0] * 11:
            print("CPF inválido.")
            return False

        # =============================
        # Validação do primeiro dígito
        # =============================
        soma = 0

        for i in range(9):
            soma += int(cpf[i]) * (10 - i)

        resto = (soma * 10) % 11
        digito1 = 0 if resto == 10 else resto

        # =============================
        # Validação do segundo dígito
        # =============================
        soma = 0

        for i in range(10):
            soma += int(cpf[i]) * (11 - i)

        resto = (soma * 10) % 11
        digito2 = 0 if resto == 10 else resto

        # Verifica os dígitos finais
        if cpf[9] == str(digito1) and cpf[10] == str(digito2):
            print("CPF validado.")
            return super().processar(pedido)

        print("CPF inválido.")
        return False

# =====================================================
# FACADE
# =====================================================

class SistemaPedido:

    def finalizar_pedido(self, pedido, tipo_pagamento):

        print("Iniciando pedido...\n")

        # Criando a cadeia de validação
        estoque = ValidarEstoque()
        valor = ValidarValorMinimo()
        cpf = ValidarCPF()

        estoque.definir_proximo(valor).definir_proximo(cpf)

        # Executando validações
        if estoque.processar(pedido):

            print("\nPedido aprovado.")

            pagamento = FabricaPagamento.criar_pagamento(
                tipo_pagamento
            )

            pagamento.pagar(pedido["valor"])

            print("Pedido finalizado com sucesso.")

        else:
            print("\nPedido cancelado.")

# =====================================================
# EXECUÇÃO
# =====================================================

pedido = {
    "valor": 150,
    "estoque": 10,
    "cpf": "52998224725"  # CPF válido para teste
}

sistema = SistemaPedido()

sistema.finalizar_pedido(
    pedido,
    "boleto"
)