class Pessoa:
    def __init__(self,id ,nome, idade, numero, email):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.numero = numero
        self.email = email

    def falar(self):
        print(f'Oi, meu nome é {self.nome}, eu tenho {self.idade} anos e meu email é {self.email}')




