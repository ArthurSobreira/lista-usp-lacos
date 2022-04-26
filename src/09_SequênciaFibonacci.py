#Faça um programa para gerar os n primeiros termos da sequência:
#1 - 1 - 2 - 3 - 5 - 8 - 13 - 21 - 34 - 55 - 89 ...

pri_term = 1
seg_term = 1
c = 0
seq = int(input('Digite quantos termos deseja ver: '))
print(f'{pri_term} - {seg_term}', end='')
while c < (seq - 2):
    ter_term = pri_term + seg_term
    print(f' - {ter_term}', end='')
    pri_term = seg_term
    seg_term = ter_term
    c += 1
