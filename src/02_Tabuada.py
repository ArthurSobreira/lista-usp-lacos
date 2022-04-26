#Faça um programa para exibir a tabuada de 0 a 9.

#Com while

num = int(input('Digite um Número para ver sua Tabuada: '))
c = 0
print('=' * 39)
while c <= 10:
    print(f'{num} * {c} = {num * c} ')
    c += 1
print('=' * 39)

#Com for

num = int(input('Digite um Número para ver sua Tabuada: '))
print('=' * 39)
for c in range(0, 11):
    print(f'{num} * {c} = {num * c}')
print('=' * 39)
