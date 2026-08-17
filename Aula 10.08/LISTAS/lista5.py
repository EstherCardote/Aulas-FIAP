produtos = ['apple tv', 'mac', 'iphone', 'apple watch', 'mac book', 'airpod']
print(produtos)

tamanho_lista = len(produtos)
print(f'A lista tem {tamanho_lista} produtos')

# Insere um valor na lista
produtos.append('apple shoes')

# Insere 2+ valores na lista
produtos.extend(['ipad', 'apple pencil'])
print(produtos)

tamanho_lista = len(produtos)
print(f'A lista agora tem {tamanho_lista} produtos')

vendas = [25,12,30,45,18,10,5,14,8]
maior_venda = max(vendas) # traz o maior valor da lista
menor_venda = min(vendas) # traz o menor valor da lista
print(f'A quantidade de item mais vendido é: {maior_venda}')
print(f'A quantidade de item menos vendido é: {menor_venda}')

total_vendas = sum(vendas)

i = vendas.index(maior_venda)
produto_mais_vendido = produtos[i]
print(f'O produto com maior venda é: {produto_mais_vendido}.')

m = vendas.index(menor_venda)
produto_menos_vendido = produtos[m]
print(f'O produto com menor venda é: {produto_menos_vendido}.')
print(f'O produto com mais vendas foi o {produto_mais_vendido}, o produto com menos venda foi o {produto_menos_vendido}, o total de vendas de todos os produtos foi de {total_vendas} unidades')