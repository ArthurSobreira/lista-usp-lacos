# Faça um programa que leia um número n e mostre na tela os n primeiros números pares e
# depois os n primeiros números ímpares.

num = int(input('Digite um Número: '))

#Caso num seja Par
if num % 2 == 0:
    for c in range(num + 2, (num * 3) + 1): #Par + 2 = Par
        if c % 2 == 0:
            print(f'{c}', end=' - ')
    print('Números Pares\n')
    for c in range(num + 1, (num * 3) + 1): #Par + 1 = Ímpar
        if not c % 2 == 0:
            print(f'{c}', end=' - ')
    print('Números Ímpares\n')

#Caso num seja Ímpar
if not num % 2 == 0:
    for c in range(num + 1, (num * 3) + 1): #Ímpar + 1 = Par
        if c % 2 == 0:
            print(f'{c}', end=' - ')
    print('Números Pares\n')
    for c in range(num + 2, (num * 3) + 2): #Ímpar + 2 = Ímpar
        if not c % 2 == 0:
            print(f'{c}', end=' - ')
    print('Números Ímpares\n')
