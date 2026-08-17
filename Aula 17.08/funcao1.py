vendas = [1200, 1500, 300, 800, 900, 100, 450]
dias = ['segunda','terca','quarta','quinta','sexta','sabado','domingo']

# Ordenar uma lista em ordem crescente
vendas.sort()
print(vendas)

# Outra forma de ordenar uma lista em ordem crescente
vendas_crescente = sorted(vendas)
print(vendas_crescente)

# Ordenar uma lista em ordem decrescente
vendas_decrescente = sorted(vendas,reverse=True)
print(vendas_decrescente)

# Contar os dias de vendas
dias_venda = len(dias)
print(f'Os dias de vendas foram: {dias_venda} 📆')

# Somar os valores de uma lista
total_vendas = sum(vendas)
print(f'O total das vendas foi: R$ {total_vendas} 💸')

maior_venda = max(vendas)
menor_venda = min(vendas)
print(f'A maior venda foi: R$ {maior_venda} ⤴️')
print(f'A menor venda foi: R$ {menor_venda} ⤵️')

for i, venda in enumerate(vendas):
    print(f'venda nº {i} : R$ {venda}')

for dia, venda in zip(dias, vendas):
    print(f'📆 {dia.upper()} : R$ {venda:.2f} 💰')