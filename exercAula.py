


def verifica_par(x):
    if(x % 2 == 0 ):
        return True
    else:
        return False
    
    

x = int(input("Digite um numero!!"))
numero = verifica_par(x)

if(numero):
    print(f"{x} é par")
else:
    print(f"{x} é impar")