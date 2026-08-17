# Escreva um programa que leia o preço de um produto e a quantidade comprada, e calcule o valor total a ser pago com desconto de 10% se a quantidade for maior que 10 unidades.
preco_unitario = float(input('Digite o preço do produto: '))
qtd_comprada = int(input('Digite a quantidade comprada: '))
total = preco_unitario * qtd_comprada

if qtd_comprada > 10:
    total = total * 0.90
    print(f'Desconto de 10% aplicado, o valor total ficou: R$ {total}')
else:
    print(f'Valor total a ser pago: R$ {total}')
