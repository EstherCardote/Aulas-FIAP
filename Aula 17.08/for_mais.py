produtos = ['tv','celular','tablet','notebook','mouse','teclado']
precos = [2500,1800,1500,3000,50,100]

# Testando FOR EACH (um a um) em uma lista de calculo de imposto
for preco in precos:
    print(f'{preco * 1.1:.2f}')

# Testando for in range (percorrendo uma lista com indice)
for i in range(len(precos)):
    produto = produtos[i]
    preco = precos[i]
    print(produto,preco)

# Testando o Enumerate
for i, preco in enumerate(precos):
    produto = produtos[i]
    print(produto,preco)
