#Escreva um programa que gera números entre 1000 e 1999 e mostra aqueles que
#divididos por 11 dão resto 5.

#Com for

print('Os números entre 1000 e 1999, que divididos por 11, dão resto 5 são: ')
for c in range(1000, 2000):
    if c % 11 == 5:
        print(c)

#Com while

print('Os números entre 1000 e 1999, que divididos por 11, dão resto 5 são: ')
c = 1000
while c < 2000:
    c += 1
    if c % 11 == 5:
        print(c)
