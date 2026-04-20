class Jogador:
    def __init__ (self):
        self.nome_jogador = ""
        self.nick = ""
        self.apelido = ""

    def cadastro_jogadores (self):
        print(f"Jogador {self.nome_jogador}: adicionado")


    def procurar_nick (self):
            print(f"Nick: {self.nome_jogador} / {self.nick} / {self.apelido}")

class Equipe:
    def __init__ (self):
        self.nome_equipe = ""
        self.jogo = ""
        self.jogadores = [] 


    def cadastro_equipe (self):
        print(f"Equipe: {self.nome_equipe} adicionado")


    def adicionar_jogador(self,jogador):
        self.jogadores.append(jogador)
        print(f"Jogador: {jogador.nome_jogador} adicionado na equipe: {self.nome_equipe}")


    def listar_equipes (self):
              print(f"Equipe: {self.nome_equipe}  Jogo: {self.jogo}  Nº Jogadores: {len(self.jogadores)} ")
    def consultar_equipes(self):
        if len(self.jogadores) == 0:
            print("Nenhum jogador na equipe.")
        else:
            for j in self.jogadores:
                print(f"Nome: {j.nome_jogador}")
                print(f"Nick: {j.nick}")
                print(f"Apelido: {j.apelido}")

    

