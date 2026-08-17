# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
s_hora = float(input('Quanto você ganha por hora: '))
q_hora = float(input('Quantas horas você trabalhou no mês: '))
t_salario = s_hora * q_hora

print(f'O seu salário esse mês será de R$ {t_salario}')