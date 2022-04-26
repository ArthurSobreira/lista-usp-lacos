# Faça um programa que leia as médias finais de vários alunos de uma turma e mostre a
# maior média, a menor média e a média aritmética da turma. O programa para quando
# encontrar uma média negativa.

med1 = float(input('Digite a Média Final do 1º aluno: '))
maior_média = menor_média = med1
cont_médias = soma_médias = 0
c = 2
if med1 >= 0:
    while True:
        med = float(input(f'Digite a Média Final do {c}º aluno: '))
        if med < 0:
            break
        if med > maior_média:
            maior_média = med
        if med < menor_média:
            menor_média = med
        cont_médias += 1
        soma_médias += med
        med_final = (soma_médias + med1) / (cont_médias + 1)
        c += 1
    print('=' * 40)
    print(f'''A MAIOR média foi {maior_média}
A MENOR média foi {menor_média}
A Média Aritmética da turma foi de {med_final:.1f}''')
    print('=' * 40)
else:
    print('=' * 83)
    print('Com a primeira média final sendo negativa, é impossível entregar os valores pedidos')
    print('=' * 83)
