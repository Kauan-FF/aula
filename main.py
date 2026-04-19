from classes import Jogador
from classes import Equipe
lista_j = []
lista_e = []

try:
    while True:
        print("MENU")
        print("1 - Cadastrar Jogadores")
        print("2 - Consultar jogadores")
        print("3 - Cadastrar equipe")
        print("4 - Consultar nomes das equipe")
        print("5 - Consultar jogadores da equipe")
        print("6 - Buscar jogador por nickname")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            vf = False
            jg = Jogador()
            jg.nome_jogador = input("Digite o nome do jogador: ")
            for veri in lista_j:
                if(jg.nome_jogador == veri.nome_jogador):
                    vf = True
                    
            if not vf:
                jg.nick = input("Digite o nick do jogador: ")
                jg.apelido = input("Digite o apelido do jogador: ")
                jg.cadastro_jogadores()
                lista_j.append(jg)
            else:
                print("Jogador já se encontra cadastrado")
        
        elif opcao == 2:
            vf = False
            vf2 = False
            eq = Equipe()
            eq.nome_equipe = input("Digite o nome da equipe: ")
            for veri in lista_e:
                if(eq.nome_equipe == veri.nome_equipe):
                    vf = True
            if not vf:
                eq.jogo = input("Digite o nome do jogo da equipe: ")
                eq.cadastro_equipe()
                lista_e.append(eq)
            else:
                print("Equipe já se encontra Cadastrada")

        elif opcao == 3:
            vf = True
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
                    vf = True
                for d in lista_e:
                    if(nome_equipe == d.nome_equipe):
                        d.adicionar_jogador(c)
                        vf2 = True
            if not vf:
                print("Nome não encontrado")
            if not vf2:
                print("Equipe não encontrada")
        elif opcao == 4:
            for e in lista_e:
                e.listar_equipes()


        elif opcao == 5:
            nome = input("Digite o nome da equipe")
            for v in lista_e:
                if(nome == v.nome_equipe):
                    v.consultar_equipes()
            

        elif opcao == 6:
            nick = input("Digite o Nick do jogador: ")
            for q in lista_j:
                if nick == q.nick:
                    q.procurar_nick()

        elif opcao == 0:
            print("Saindo....")

        else:
            print("Digite um numero de 1 a 6")
except Exception as erro:
    print(f"DEU erro {erro}")