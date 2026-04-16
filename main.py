from classes import Estudante
from classes import Equipe

equipes = []
jogadores = []

while True:
    print("\n=== MENU ===")
    print("1 - Cadastrar Jogadores")
    print("2 - Consultar jogadores")
    print("3 - Cadastrar equipe")
    print("4 - Consultar nomes das equipe")
    print("5 - Consultar jogadores da equipe")
    print("6 - Buscar jogador por nickname")
    print("7 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome_jg = input("Digite o nome do jogador: ")
        nick = input("Digite o nick do jogador: ")
        ape = input("Digite o apelido do jogador: ")

        jogador = Estudante(nome_jg, nick, ape)
        jogadores.append(jogador)
        jogador.cadastro_jogadores()
    
    elif opcao == 2:
        nome_eq = input("Digite o nome da equipe: ")
        jg = input("Digite o nome do jogo da equipe: ")
        equipe= Equipe(nome_eq,jg)
        equipes.append(equipe)
        equipe.cadastro_equipe()

    elif opcao == 3:
        equi = input("Digite o nome da equipe")
        for eq in equipes:
            if(equi == eq.nome_equipe):
                nome = input("Digite o nome do jogador")
                for j in jogadores:
                    if(nome == j.nome_jogador):
                        eq.jogadores.append(j)
                        equipe.cadastro_equipe()

    elif opcao == 4:
        if len(equipes) > 0:
            equipes[0].consultar_equipes(equipes)
            

    elif opcao == 5:
        nome = input("Digite o nome da equipe")
        for x in equipes:
            if( nome == x.nome_equipe): 
                x.consultar_membros()