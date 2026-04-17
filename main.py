from classes import Jogador
from classes import Equipe
lista_j = []
lista_e = []
while True:
    print("\n=== MENU ===")
    print("1 - Cadastrar Jogadores")
    print("2 - Consultar jogadores")
    print("3 - Cadastrar equipe")
    print("4 - Consultar nomes das equipe")
    print("5 - Consultar jogadores da equipe")
    print("6 - Buscar jogador por nickname")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        jg = Jogador()
        jg.nome_jogador = input("Digite o nome do jogador: ")
        jg.nick = input("Digite o nick do jogador: ")
        jg.apelido = input("Digite o apelido do jogador: ")
        jg.cadastro_jogadores()
        lista_j.append(jg)
    
    elif opcao == 2:
        eq = Equipe()
        eq.nome_equipe = input("Digite o nome da equipe: ")
        eq.jogo = input("Digite o nome do jogo da equipe: ")
        eq.cadastro_equipe()
        lista_e.append(eq)

    elif opcao == 3:
        print("Lista de Jogadores Disponiveis")
        for a in lista_j:
            print(f"Jogadores: {a.nome_jogador} disponiveis ")
        print("Lista de Equipes Disponiveis")
        for b in lista_e:
            print(f"Equipes: {b.nome_equipe} disponiveis ")
        
        jogadores = input("Digite o nome do Jogador")
        for c in lista_j:
                if(jogadores == c.nome_jogador):
                    nome_equipe = input("Digite o nome da equipe")
                    for d in lista_e:
                        if(nome_equipe == d.nome_equipe):
                            d.adicionar_jogador(c)

    elif opcao == 4:
        for e in lista_e:
            e.listar_equipes()


    elif opcao == 5:
       nome = input("Digite o nome da equipe")
       for v in lista_e:
           if(nome == v.nome_equipe):
               v.consultar_equipes()
        

    elif opcao == 6:
        pass
    elif opcao == 0:
        print("Saindo....")

    else:
        print("Digite um numero de 1 a 6")
