# Importa suporte a classes abstratas
from abc import ABC, abstractmethod

# =========================
# IMPLEMENTAÇÃO (Renderização)
# =========================
class Renderizador(ABC):
    """
    Interface que define como uma forma será desenhada.
    Essa é a parte que pode variar independentemente.
    """

    @abstractmethod
    def desenhar_circulo(self, x, y, raio):
        pass  # Método abstrato para desenhar círculo

    @abstractmethod
    def desenhar_quadrado(self, x, y, tamanho):
        pass  # Método abstrato para desenhar quadrado


# =========================
# IMPLEMENTAÇÕES CONCRETAS
# =========================
class OpenGLRenderer(Renderizador):
    """
    Implementação concreta usando OpenGL
    """

    def desenhar_circulo(self, x, y, raio):
        print(f"OpenGL: desenhando círculo em ({x},{y}) com raio {raio}")

    def desenhar_quadrado(self, x, y, tamanho):
        print(f"OpenGL: desenhando quadrado em ({x},{y}) com tamanho {tamanho}")


class DirectXRenderer(Renderizador):
    """
    Implementação concreta usando DirectX
    """

    def desenhar_circulo(self, x, y, raio):
        print(f"DirectX: desenhando círculo em ({x},{y}) com raio {raio}")

    def desenhar_quadrado(self, x, y, tamanho):
        print(f"DirectX: desenhando quadrado em ({x},{y}) com tamanho {tamanho}")


# =========================
# ABSTRAÇÃO (Forma)
# =========================
class Forma(ABC):
    """
    Classe base das formas.
    Aqui ocorre o Bridge: a forma possui um renderizador.
    """

    def __init__(self, renderizador):
        self.renderizador = renderizador

    @abstractmethod
    def desenhar(self):
        pass


# =========================
# ABSTRAÇÕES REFINADAS
# =========================
class Circulo(Forma):
    """
    Forma concreta: Círculo
    """

    def __init__(self, x, y, raio, renderizador):
        super().__init__(renderizador)
        self.x = x
        self.y = y
        self.raio = raio

    def desenhar(self):
        self.renderizador.desenhar_circulo(self.x, self.y, self.raio)


class Quadrado(Forma):
    """
    Forma concreta: Quadrado
    """

    def __init__(self, x, y, tamanho, renderizador):
        super().__init__(renderizador)
        self.x = x
        self.y = y
        self.tamanho = tamanho

    def desenhar(self):
        self.renderizador.desenhar_quadrado(self.x, self.y, self.tamanho)


# =========================
# CLIENTE (Uso do sistema)
# =========================
if __name__ == "__main__":
    opengl = OpenGLRenderer()
    directx = DirectXRenderer()

    circulo1 = Circulo(10, 20, 5, opengl)
    circulo2 = Circulo(30, 40, 10, directx)
    quadrado1 = Quadrado(0, 0, 15, opengl)
    quadrado2 = Quadrado(5, 5, 8, directx)

    print("\n--- Desenhando Formas ---")
    circulo1.desenhar()
    circulo2.desenhar()
    quadrado1.desenhar()
    quadrado2.desenhar()