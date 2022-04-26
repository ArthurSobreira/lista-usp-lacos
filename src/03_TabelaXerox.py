#Faça um programa para ler um número real e exibir uma tabela em que o número
#apareça multiplicado até 200, sendo 10 em cada linha.

#Com while
num = float(input('Digite um Número: '))
c = 1
while c <= 200:
    print(f'| {c} * {num} = {num * c:.1f}', end=' | ')
    if c % 10 == 0:
        print('\n')
    c += 1

#Com for

num = float(input('\nDigite um Número: '))
for c in range(1, 201):
    print(f'| {c} * {num}= {num * c:.1f}', end=' | ')
    if c % 10 == 0:
        print('\n')
