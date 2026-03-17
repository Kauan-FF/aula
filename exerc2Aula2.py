def calcDesconto(precos, p):
    for i in range(0,len(precos)):
        valor = precos[i]  * (p/100)
        valor = precos[1] - p
        precos[i] = valor 
    return precos
indiceProd = 0
produtos = [""] * 10
precos = []



opc = 0
while(opc != 4):
    print("MENU: \n 1- Cadastrar Produto \n 2- Listar Produtos \n 3-Aplicar Desconto \n 3-Aplicar Desconto \n 4- Sair do Programa")
    opc = int(input("Digite um numero de 1 a 4 "))
    if(opc == 1):
        print("1- Cadastrar Produto")
        nome = input("Nome: ")
        valor = float(input("Valor: R$"))
        produtos[indiceProd] = nome
        indiceProd +=1
        precos.append(valor)


    elif(opc == 2):
        print("2- Listar Produtos")
        for i in range(0, len(precos)):
            print(produtos[i], "-", precos[i])

    elif(opc == 3):
        print("3-Aplicar Desconto")
        desconto = int(input("Digite a porcentagem do desconto"))
        preco_final = calcDesconto(precos, desconto)
        for i in range(0, len(precos)):
            print(produtos[i], "-", preco_final[i])

    elif(opc == 4):
        print("4- Sair do Programa")
    else:
        print("Digite um numero de 1 a 4")
    