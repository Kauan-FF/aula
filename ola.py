import random

escolha = 1
while escolha  !=0:
    
    print("VAMOS JOGAR JOKEMPO \nDigite 1 para Pedra \nDigite 2 para Tesoura \nDigite 3 para Papel  \nDigite 0 para Sair")
    escolha = int(input("Vamos começar"))

    x = random.randint(0,3)
    if escolha ==  x  :
        print("Empate")
    elif escolha == 1 and x == 3 or  escolha == 2 and x == 1 or  escolha == 3 and x == 2:
        print("Perdeu")
    elif escolha == 1 and x == 2 or escolha == 2 and x == 3 or  escolha == 3 and x == 1:
        print("ganhou")
    else:
        print("Digite um numero de 1 a 4")
print("Voce saiu :(")