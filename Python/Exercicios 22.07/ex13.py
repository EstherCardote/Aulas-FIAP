# Escreva um programa que leia dois números inteiros e troque os seus valores, ou seja, o primeiro deve ficar com o valor do segundo e vice-versa
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

print(f'Valores originais: num1: {num1} num2: {num2}')

a = num1
num1 = num2
num2 = a

print(f'Valores trocados: num1: {num1} num2: {num2}')

