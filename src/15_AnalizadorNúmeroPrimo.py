#Faça um programa que leia um número n e imprima se ele é primo ou não. (um número
#primo tem apenas 2 divisores: 1 e ele mesmo, O número 1 não é primo).

#Ultilizando laço for

num = int(input('Digite um Número: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        cont += 1
if cont == 2:
    print(f'\n{num} É Primo, pois possuí apenas dois divisores reais, ele mesmo e 1.')
elif num == 1:
    print('O número 1 não é considerado Primo.')
else:
    print(f'\n{num} Não é Primo, pois possui mais de 2 divisores reais.')

#Ultilizando laço while

num = int(input('Digite um Número: '))
c = 1
cont = 0
while c <= num:
    if num % c == 0:
        cont += 1
    c += 1
if cont == 2:
    print(f'\n{num} É Primo, pois possuí apenas dois divisores reais, ele mesmo e 1.')
elif num == 1:
    print('O número 1 não é considerado Primo.')
else:
    print(f'\n{num} Não é Primo, pois possui mais de 2 divisores reais.')
