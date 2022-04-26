#Faça um programa que calcula o produto dos números digitados pelo usuário. O
#programa deve permitir que o usuário digite uma quantidade não determinada de
#números. O programa encerra quando o usuário digita o valor zero.

prod = 1
c = 1
while True:
    num = int(input(f'Digite Um Valor: '))
    if num == 0:
        if c == 1:
            prod *= num
        break
    c += 1
    prod *= num
print(f'O produto dos Valores é {prod}')
