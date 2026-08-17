nome = input('Digite um nome: ')

for i in range(5):
    print(nome)

for i in range(10):
    print(i)

nome = 'Maria'
contador = 0

for i in range(10):
    print(f'{contador} - {nome}')
    contador = contador+1

nome = 'Maria'

for i in range(10):
    print(i, nome)