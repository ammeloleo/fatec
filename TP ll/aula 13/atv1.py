class Veiculo:
    def __init__(self, marca, modelo, cor):
        # Estado Intrínseco: compartilhado entre objetos iguais
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    def exibir(self, placa, vaga):
        # Recebe o Estado Extrínseco por parâmetro
        print(f"Veículo: {self.marca} {self.modelo} ({self.cor}) | Placa: {placa} | Vaga: {vaga}")

class FabricaVeiculo:
    _veiculos = {}

    @classmethod
    def get_veiculo(cls, marca, modelo, cor):
        # Cria uma chave única para identificar o conjunto de atributos
        chave = (marca, modelo, cor)
        
        if chave not in cls._veiculos:
            print(f"--- Criando novo objeto Flyweight: {marca} {modelo} {cor} ---")
            cls._veiculos[chave] = Veiculo(marca, modelo, cor)
        
        return cls._veiculos[chave]
# Instanciando a fábrica
fabrica = FabricaVeiculo()

# Criando 5 veículos (note que alguns compartilham o estado intrínseco)
v1 = fabrica.get_veiculo("Fiat", "Uno", "Prata")
v2 = fabrica.get_veiculo("Fiat", "Uno", "Prata") # Compartilhado
v3 = fabrica.get_veiculo("Honda", "Civic", "Preto")
v4 = fabrica.get_veiculo("Volkswagen", "Voyage", "Branco")
v5 = fabrica.get_veiculo("Honda", "Civic", "Preto") # Compartilhado

print("\n--- Exibindo Dados no Terminal ---")
v1.exibir("ABC1234", 12)
v2.exibir("XYZ9876", 18)
v3.exibir("AAA1111", 22)
v4.exibir("BBB2222", 5)
v5.exibir("CCC3333", 40)

# Verificação de compartilhamento
print(f"\nTotal de objetos Flyweight criados: {len(fabrica._veiculos)}")