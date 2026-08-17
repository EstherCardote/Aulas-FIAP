import statistics

vendas = [150,90,2000,30,120,3,3,4,4,2,2,2]
media_vendas = (sum(vendas) / len(vendas))
print(media_vendas)

media = statistics.mean(vendas)
print(f'A média é: {media} 🥰')

mediana = statistics.median(vendas)
print(f'A mediana é: {mediana} 😎')

modal = statistics.mode(vendas)
print(f'O modal é: {modal} 😋')