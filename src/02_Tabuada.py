#Faça um programa para exibir a tabuada de 0 a 9.

def multi_table(number):
    for c in range(11):
        print(f'{number} * {c} = {number * c}')


def main():
    num = int(input('Input a number: '))
    multi_table(num)


if __name__ == '__main__':
    main()
