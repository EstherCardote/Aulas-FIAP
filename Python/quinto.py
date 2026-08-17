peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura * altura)
print(f'O seu imc é {imc}')

if imc < 15:
    print('Você esta esquelético!')
elif imc >= 15 and imc <= 18.5:
    print('Você esta abaixo do peso!')
elif imc >= 18.6 and imc <= 24.9:
    print('Você esta no peso normal!')
elif imc >= 25 and imc <= 29.9:
    print('Você esta acima do peso!')
elif imc >= 30 and imc <= 39.9:
    print('Você esta na obesidade grau I!')
else:
    print('Você está na obesidade grau II!')

