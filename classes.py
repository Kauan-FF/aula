class Jogador:
    def __init__ (self,nome_jg, nick,ape):
        self.nome_jogador = nome_jg
        self.nick = nick
        self.apelido = ape


    def cadastro_jogadores (self):
        print(f"Jogador {self.nome_jogador}: adicionado")

    def consultar_jogadores (self,lista):
        for estudante in lista:
            print(f"Jogador: {estudante.nome_jogador}/ nickname: {estudante.nick}/ Apelido {estudante.apelido}")

    def procurar_nick (self):
        print(f"Nick: {self.nome_jogador} / {self.nick} / {self.apelido}")

class Equipe:
    def __init__ (self,nome_eq,jg):
        self.nome_equipe = nome_eq
        self.jogo = jg 
        self.jogadores = []


    def cadastro_equipe (self):
        print(f"Equipe: {self.nome_equipe}: adicionado")


    def adicionar_jogador(self):
        print(f"Jogador: {self.jogadores} adicionado")


    def consultar_membros (self):
        if(len(self.jogadores) >= 1):
            print(f"Nome da equipe: {self.nome_equipe}")
            for i in self.jogadores:
                print(f"Jogador: {i.jogadores}")
        else:
            print("Nenhuma equipe cadastrada")

    def consultar_equipes(self):
                print(f"Nome: {self.nome_equipe} ")
        

    
    

