class Livro:
    def __init__(self,titulo,disponivel):
        self.titulo = titulo
        self.disponivel = disponivel

    def emprestar(self):
        nome = input("Digite o nome do Livro: ")
        if(nome == self.titulo and self.disponivel == True):
            print("livro pode ser imprestado")
            self.sisponivel = False
        elif(nome == self.titulo and self.disponivel == False):
            print("Livro não pode ser emprestado")


        
    
    def devolver(self):
        nome = input("digite o nome do Livro")
        if(nome == self.titulo ):
            self.disponivel = True
        else:
            print("Titulo não encontrado")


titulo = "one piece"
disponivel = True
livro1 =Livro(titulo,disponivel)
escolha = int(input("Digite 1 para emprestar e 2 para devolver"))
if(escolha == 1):
    livro1.emprestar()
elif(escolha == 2):
    livro1.devolver()
else: 
    print("Opção Invalida")







