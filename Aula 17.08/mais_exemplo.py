vendas = [
    ['João',15000],
    ['Maria',20000],
    ['Jose',25000],
    ['Jorge',13000],
    ['Gabriel',10000],
    ['Lucas',5000],
]

meta_venda = 10000

for item in vendas:
    if item[1] >= meta_venda:
        print(f'Vendedor {item[0]} bateu a meta 🙌 Fez {item[1]} em vendas 💸.')