funcionarios = [
    "Ana Silva", "Bruno Santos", "Carlos Oliveira", "Diana Souza", "Eduardo Lima",
    "Fernanda Costa", "Gabriel Pereira", "Helena Almeida", "Igor Ribeiro", "Júlia Carvalho",
    "Lucas Fernandes", "Mariana Rodrigues", "Nicolas Martins", "Olívia Ramos", "Pedro Castro",
    "Larissa Mendes", "Rafael Rocha", "Sofia Azevedo", "Thiago Nogueira", "Vitória Morais",
    "Matheus Cardoso", "Beatriz Farias", "Gustavo Araujo", "Camila Correia", "Daniel Duarte",
    "Isabela Freitas", "Leonardo Vieira", "Natália Barreto", "Rodrigo Cunha", "Vanessa Pires"
]

for funcionario in funcionarios:
    print(funcionario)

for i, funcionario in enumerate(funcionarios):
    print(f'O nome do funcionário {i} é: {funcionario}')

# Usando exemplo de produtos em estoque
produtos = ['coca','pepsi','guarana','sprite','fanta','dolly','tubaina']
estoque = [550,300,500,450,800,650,200]
estoque_min = 500

for i, qtde in enumerate(estoque):
    if qtde < estoque_min:
        print(f'O produto {produtos[i]} está abaixo do estoque mínimo. Temos apenas {estoque[i]} unidades.')
