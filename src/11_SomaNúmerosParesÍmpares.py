#Faça um programa que leia vários inteiros positivos e mostre, no final, a soma dos
#números pares e a soma dos números ímpares. O programa para quando entrar um número
#maior que 1000.

c = 1
soma_p = 0
soma_i = 0
while True:
    num = int(input(f'Digite o {c}º Valor: '))
    if num > 1000:
        break
    if num % 2 == 0:
        soma_p += num
    else:
        soma_i += num
    c += 1
print(f'A soma dos números Pares que você digitou é {soma_p}')
print(f'A soma dos números Ímpares que você digitou é {soma_i}')
