#Dado um número n inteiro e positivo, dizemos que n é perfeito se n for igual à soma de
#seus divisores positivos diferentes de n. Construa um programa que verifica se um
#dado número é perfeito.

num = int(input('Digite um Número: '))
soma = 0
for c in range(num-1, 0, -1):
    if num % c == 0:
        soma += c
        div = print(c, end=' - ')
print(f'Divisores de {num}')
if soma == num:
    print(f'\n{num} é perfeito, pois a soma de seus divisores é {soma}')
else:
    print(f'\n{num} não é perfeito, pois a soma de seus divisores é {soma}')
