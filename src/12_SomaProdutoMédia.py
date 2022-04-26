# Faça um programa que leia vários conjuntos de três valores reais e mostre para cada
# conjunto: sua soma, seu produto e sua média. O programa para quando um conjunto não
# entrar com seus valores em ordem crescente.

c = 1
while True:
    print('=' * 10, f'Conjunto {c}', '=' * 10)
    prod = 1
    soma = menor_val = meio_val = maior_val = 0
    for i in range(1, 4):
        val = int(input(f'Digite o {i}º Valor: '))
        if i == 1:
            menor_val = val
        if i == 2:
            meio_val = val
        if i == 3:
            maior_val = val
        soma += val
        prod *= val
    if not menor_val < meio_val < maior_val:
        break
    print(f'A Soma dos valores digitados é {soma}')
    print(f'A Média dos valores digitados é {soma / 3}')
    print(f'O Produto dos valores digitados é {prod}')
    c += 1
print('=' * 66)
print('Fim do Programa, os valores digitados não estão em ordem crecente.')
print('=' * 66)
