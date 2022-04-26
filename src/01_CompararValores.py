#Escreva um programa que lê 15 valores reais, encontra o maior e o menor deles e
#mostra o resultado.

maior_num = 0
menor_num = 0
for c in range(1, 16):
    val = int(input(f'Digite o {c}º Valor: '))
    if c == 1:
        maior_num = val
    if val > maior_num:
        maior_num = val
    if c == 1:
        menor_num = val
    if val < menor_num:
        menor_num = val

print(f'Dos 15 Números que você digitou, {maior_num} é o MAIOR')
print(f'Dos 15 Números que você digitou, {menor_num} é o MENOR')
