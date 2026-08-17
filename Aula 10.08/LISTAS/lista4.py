produtos = ['apple tv', 'mac', 'iphone', 'apple watch', 'mac book', 'airpod']
print(produtos)

# Para inserir um valor em uma nova posição dentro da lista
produtos.append('iphone 17')
print(produtos)

# Substituir um valor por outro na mesma posição da lista
produtos[1] = 'tac'
print(produtos)

# Remove um item da lista
produtos.remove('iphone')
print(produtos)

# Remover um valor externo 
produto_apagado = input('Digite o nome do produto a ser removido: ').lower()
if produto_apagado in produtos:
    produtos.remove(produto_apagado)
    print(produtos)
else:
    print('Produto Inexistente na Lista!')    