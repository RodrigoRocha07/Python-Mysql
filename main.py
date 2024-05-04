from crud_bd import *
from pessoa import Pessoa

lista = listar()
objetos = []

# Alocar dentro da lista 'objetos' cada elemento de "lista" transformando cada um em um objeto da classe 'Pessoa'
for pessoa in lista:
    pessoa = Pessoa(pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4])
    objetos.append(pessoa)


def main():
    for pessoa in objetos:
        pessoa.falar()
    


if __name__ == "__main__":
    main()
