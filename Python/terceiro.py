nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Diite a segunda nota: '))

media = (nota1 + nota2) / 2
print(f'A media das notas é: {media}')

if media >= 7:
    print('Aluno Aprovado')
elif media >=6:
    print('Aluno de Recuperação')
else:
    print('Aluno Reprovado')