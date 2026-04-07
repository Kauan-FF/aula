class Aluno:
    def __init__(self,nome,idade,curso, ra, notas):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.ra = ra
        self.notas = notas
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e faço o curso de {self.curso}.")
        while(self.ra == ""):
            print("Esse aluno não tem RA")
            
            self.ra = input("Digite seu RA")
        
        print(f"O RA  é {self.ra}")
        
        
    def calcular_media(self, ):
        soma = 0.0
        for x in range(0, len(self.notas)):
            soma += self.notas[x]
        media = soma/len(self.notas)
        print(media)
            

        


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
curso = input("Digite o nome do seu curso: ")
ra = input("Digite o seu RA: ")
notas = [0] * 3
for i in range(3):
    notas[i] = float(input(F"Digete sua nota {i + 1}"))


aluno1 = Aluno(nome,idade,curso, ra,notas)
aluno1.apresentar()
aluno1.calcular_media()




