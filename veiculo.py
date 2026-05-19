class Veiculo:
    def __init__(self, marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade_atual = velocidade

    def acelerar(self):
        self.velocidade_atual += 20

    def frear(self):
        if(self.velocidade_atual >= 10):
            self.velocidade_atual -= 10
        else: 
            self.velocidade_atual = 0
            print("Não foi possível diminuir, pare o carro")

    def info(self):
        print(f"Marca  = {self.marca}  \n Modelo = {self.modelo} \n Ano = {self.ano} \n Velocidade atual = {self.velocidade_atual}")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, velocidade, numero_portas):
        super().__init__( marca, modelo, ano, velocidade)
        self.portas = numero_portas
    
    def acelerar(self):
        self.velocidade_atual += 15
    
    def info(self):
        print(f"Marca  = {self.marca}  \n Modelo = {self.modelo} \n Ano = {self.ano} \n Velocidade atual = {self.velocidade_atual}\n Portas = {self.portas}")

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, velocidade, cilindradas):
        super().__init__( marca, modelo, ano, velocidade)
        self.cilindradas = cilindradas

    def acelerar(self):
        self.velocidade_atual += 20

    def frear(self):
        if(self.velocidade_atual >= 15):
            self.velocidade_atual -= 15
        else: 
            self.velocidade_atual = 0
            print("Não foi possível diminuir, pare o carro")

    def info(self):
        print(f"Marca  = {self.marca}  \n Modelo = {self.modelo} \n Ano = {self.ano} \n Velocidade atual = {self.velocidade_atual}\n Cilindradas = {self.cilindradas}")
