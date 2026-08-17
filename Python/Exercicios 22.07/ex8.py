# Vamos criar um conversor de temperatura. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. Fórmula: C = 5/9 × (F − 32)
f = float(input('Digite a temperatura em Fahrenheit: '))
c = (5/9) * (f - 32)

print(f'Agora está {f:.1f}°F ou {c:.1f}°C')