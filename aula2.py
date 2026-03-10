x = int(input("Digite um numero de 1 a 10 para ver a  sua Tabuada"))

for cont in range(1, 11):
    resp = x * cont
    print(f"{x} X {cont} = {resp}")