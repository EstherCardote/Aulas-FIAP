"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total. (Para simplificar, por enquanto não se preocupe em arredondar a quantidade de latas.)"""

area_metros = float(input('Digite o tamanho em m² da área a ser pintada: '))
litros_necessarios = area_metros / 3
qtd_latas = litros_necessarios / 18
preco_total = qtd_latas * 80

print(f'Quantidade de latas necessárias: {qtd_latas:.1f}')
print(f'Preço total da tinta: R$ {preco_total:.260f}')