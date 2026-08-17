# Combinando FOR com IF

vendas = [1200, 1500, 300, 800, 900, 100, 450, 3000, 700, 5000]
meta = 1200

# Quais valores bateram a meta
for venda in vendas:
    if venda >= meta:
        print(venda)

# Quantos valores bateram a meta
metas_batidas = 0
for venda in vendas:
    if venda >= meta:
        metas_batidas += 1
        print(metas_batidas)
