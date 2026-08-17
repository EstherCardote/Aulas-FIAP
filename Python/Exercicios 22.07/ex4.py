# Faça um Programa que peça as 4 notas bimestrais de um aluno e mostre a média de todas as notas.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'Sua média é: {media}')