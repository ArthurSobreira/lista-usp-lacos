# Faça um programa que leia um número n e mostre na tela os n primeiros números primos.

num = int(input('Digite quantos números Primos deseja ver: '))
a = 2
div_a = 0
lim = 0
for a in range(a, 1000): #Limite de Primos entre 2 e 1000
    b = 1
    for b in range(b, a + 1):
        if a % b == 0:
            div_a += 1
    if div_a == 2:
        lim += 1
        for i in range(lim <= num):
            print(a)
        div_a = 0
    else:
        div_a = 0
