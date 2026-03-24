class Campus:
    def __init__(self):
        self.nome =  ""
        self.endereco =  ""
    
    def __str__(self):
        return f"campus: {self.nome}"
    

class Estudantes:
    def __init__(self):
        self.nome = ""
        self.cpf = ""
        self.data_nasc = ""

    def __str__(self):
        return f"Estudantes:{ self.nome}"
    

    def apresentar(self):
        print(f"O(a) {self.nome} nasceu em {self.data_nasc}") 
        if(self.cpf == ""):
            print("O(a) estudante não cadastrou CPF")
        else:
            print(f"CPF: {self.cpf[0:3]} ...")

    
kauan= Estudantes()
kauan.nome = "Kauan Campois"
kauan.cpf = "898.789.654-09"
kauan.data_nasc = "06/04/2009"
kauan.apresentar()