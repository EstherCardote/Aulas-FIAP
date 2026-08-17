# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. Fórmula: F = 9/5 × C + 32 
c = float(input('Digite a temperatura em °C: '))
f = 9/5 * c + 32

print(f'Agora está {c:.2f}°C ou {f:.2f}°F')