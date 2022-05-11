#Escreva um programa que lê 15 valores reais, encontra o maior e o menor deles e
#mostra o resultado.


def main():
    my_list = []
    for c in range(1, 16):
        val = int(input(f'Input the {c}st Value: '))
        my_list.append(val)

    print(f'Of the 15 numbers you entered, {max(my_list)} is the Biggest.')
    print(f'Of the 15 numbers you entered, {min(my_list)} is the Smallest.')


if __name__ == '__main__':
    main()
