# Crie um programa que leia o valor do depósito mensal em uma poupança e a taxa de juros mensal, e calcule o montante após 12 meses.
dep_mensal = float(input('Digite o valor do depósito mensal: '))
tx_juros = float(input('Digite o taxa de juros mensal: '))

montante = (dep_mensal*12) * tx_juros
print(f'O montante aculumado em 12 meses foi de: R$ {montante}')