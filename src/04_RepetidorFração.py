# Faça um programa que calcula e escreve a seguinte soma:
# soma = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50.

my_list = list()
x = 1  # Variável Numerador
y = 1  # Variável Denominador
while x <= 99 and y <= 50:
    print(f'{x}/{y} + ', end='')
    fra = x/y
    my_list.append(fra)
    x += 2
    y += 1
print(f'\nA soma das frações é {sum(my_list)}')
