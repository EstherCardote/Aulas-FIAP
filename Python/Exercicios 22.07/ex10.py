"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Em seguida:
a)	Calcule o salário bruto (horas × salário por hora).
b)	Calcule o desconto do IR (11% do salário bruto).
c)	Calcule o desconto do INSS (8% do salário bruto).
d)	Calcule o desconto do sindicato (5% do salário bruto).
e)	Calcule o salário líquido (salário bruto − descontos)."""

s_hora = float(input('Quanto você ganha por hora: '))
q_hora = float(input('Quantas horas você trabalhou no mês: '))

s_bruto = s_hora * q_hora
print(f'Salário bruto: {s_bruto}')
ir = s_bruto * 0.11
print(f'Desconto de IR: {ir}')
inss = s_bruto * 0.08
print(f'Desconto de INSS: {inss}')
sindicato = s_bruto * 0.05
print(f'Desconto do sindicato: {sindicato}')
s_liquido = s_bruto - ir - inss - sindicato
print(f'Salário liquido: R$ {s_liquido}')
