from abc import ABC, abstractmethod

# Interface
class Imagem(ABC):
    @abstractmethod
    def exibir(self):
        pass


# Objeto real (pesado)
class ImagemReal(Imagem):
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.carregar_do_disco()

    def carregar_do_disco(self):
        print(f"Carregando {self.nome_arquivo} do disco...")

    def exibir(self):
        print(f"Exibindo {self.nome_arquivo}")


# Proxy
class ProxyImagem(Imagem):
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.imagem_real = None

    def exibir(self):
        if self.imagem_real is None:
            self.imagem_real = ImagemReal(self.nome_arquivo)
        self.imagem_real.exibir()


# Uso
imagem = ProxyImagem("foto.png")

# Não carrega ainda
print("Imagem criada")

# Carrega somente aqui
imagem.exibir()