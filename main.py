from classes import Jogador
from classes import Equipe

equipes = []
jogadores= []

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

        jogador = Jogador(nome_jg, nick, ape)
        jogadores.append(jogador)
        jogador.cadastro_jogadores()
    
    elif opcao == 2:
        nome_eq = input("Digite o nome da equipe: ")
        jg = input("Digite o nome do jogo da equipe: ")
        equipe= Equipe(nome_eq,jg)
        equipes.append(equipe)
        equipe.cadastro_equipe()

    elif opcao == 3:
        for cont in range (len(equipes)):
            print(f"Nome: {cont.nome_equipe}" )
            


        equi = input("Digite o nome da equipe")
        for eq in equipes:
            if(equi == eq.nome_equipe):
                nome = input("Digite o nome do jogador")
                for j in jogadores:
                    if(nome == j.nome_jogador):
                        eq.jogadores.append(j)
                        equipe.adicionar_jogador()

    elif opcao == 4:
        if(len(equipes) >= 1):
            for equipe in equipes:
                equipe.consultar_equipes()
        else:
            print("Nenhuma equipe cadastrada")

    elif opcao == 5:
        nome = input("Digite o nome da equipe")
        for x in equipes:
            if( nome == x.nome_equipe): 
                x.consultar_membros()


    elif opcao == 6:
        busca = input("Digite o nick do jogador")
        if(len(jogadores) == 0):
            print("Nenhum jogador cadastrado")
            for k in jogadores:
                if(busca == k.nick ):
                    k.procurar_nick()

                else:
                    print("Jogador não encontrado")
    elif opcao == 0:
        print("Saindo....")

    else:
        print("Digite um numero de 1 a 6")
