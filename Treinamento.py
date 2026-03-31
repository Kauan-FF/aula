class Cliente:
    def __init__(self):
        self.nome = ""
        self.dt_nasc = ""
        self.cpf = ""

    def apresentar(self):
        print(
            f"Cliente: {self.nome} \n data de nascimento: {self.dt_nasc}\n CPF: {self.cpf[0:3]}...")


class Conta:
    def __init__(self):
        self.numero_conta = ""
        self.cliente = ""
        self.saldo = 0.0

    def deposito(self, valor):
        valor = float(input("Digite o valor do deposito"))
        self.saldo += valor
        print("Deposito efetuado")

    def saque(self, saque):
        saque = float(input("Digite o valor do saque"))
        if (saque > self.saldo):
            print("Saldo Invalido")
        else:
            self.saldo -= saque
            print("Saque efetuado")

    def transferencia(self, tf, destino):
        tf = float(input("Digite o valor da transferência"))
        if (tf > self.saldo):
            print("Transferencia Invalida")
        else:
            self.saldo -= tf
            destino.saldo += tf
            print("Transferencia efetuada")


kauan = Cliente()
kauan.nome = "Kauan dos Santos Campois"
kauan.dt_nasc = "06/04/2009"
kauan.cpf = "145.903.189-03"
kauan.apresentar()

conta1 = Conta()
conta1.numero_conta = 1
conta1.cliente = kauan
conta1.saldo = 1000.99

conta2 = Conta()
conta2.numero_conta = 2
conta2.cliente = kauan
conta2.saldo = 500.00

conta1.saque(0)
conta1.deposito(0)
conta1.transferencia(0, conta2)

print(f"Saldo conta1: {conta1.saldo}")
