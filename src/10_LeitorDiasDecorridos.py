# Escrever um programa que calcula o número de dias decorridos entre duas datas
# lidas: a data mais antiga e a data mais recente. Considerar a ocorrência de anos bissextos.
# Considerar o seguinte intervalo para o valor do ano fornecido: 1950-1996 (1952 foi um
# ano bissexto)


def apart(msg):
    size = len(msg) + 4
    print('=' * size)
    print(f'{msg:^{size}}')
    print('=' * size)


def bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return True


def main():
    mes_30 = ['Abril', '4', 4, 'Junho', '6', 6, 'Setembro', '9', 9, 'Novembro', '11', 11]
    mes_31 = ['Janeiro', '1', 1, 'Março', '3', 3, 'Maio', '5', 5, 'Julho', '7', 7, 'Agosto', '8', 8, 'Outubro', '10', 10,
              'Dezembro', '12', 12]
    mes_28_29 = ['Fevereiro', '2', 2]

    apart('Digite a Data Inicial')

    while True:  # Validar o Ano Inicial...
        ano_inicial = int(input('> Ano: '))
        if 3000 >= ano_inicial >= 1601:
            break
        else:
            if ano_inicial <= 1600:
                print('Ano Inválido (Anos abaixo de 1601 não são permitidos).')
            if ano_inicial >= 3001:
                print('Ano Ínválido (Anos acima de 3000 não são permitidos).')

    while True:  # Validar o Mês Inicial...
        mes_inicial = str(input('> Mês: ')).strip().capitalize()
        if mes_inicial in mes_28_29 or mes_inicial in mes_30 or mes_inicial in mes_31:
            break
        else:
            print('Mês inválido,tente novamente.')

    while True:  # Validar o Dia Inicial...
        dia_inicial = int(input('> Dia: '))

        # Para Caso o Ano Seja Bissexto...
        if bissexto(ano_inicial):
            if mes_inicial in mes_28_29 and 1 <= dia_inicial <= 29:
                break
            else:
                if mes_inicial in mes_28_29:
                    if dia_inicial > 29:
                        print(f'{ano_inicial} é um ano bissexto, logo Fevereiro possui apenas 29 dias, tente novamente.')
                    if dia_inicial < 0:
                        print('Dias Negativos não são permitidos, tente novamente.')
                    if dia_inicial == 0:
                        print('0 não é um dia permitido, tente novamente.')

            if mes_inicial in mes_30 and 1 <= dia_inicial <= 30:
                break
            else:
                if mes_inicial in mes_30:
                    if dia_inicial > 30:
                        print(f'O mês escolhido possui apenas 30 dias, tente novamente.')
                    if dia_inicial < 0:
                        print('Dias Negativos não são permitidos, tente novamente.')
                    if dia_inicial == 0:
                        print('0 não é um dia permitido, tente novamente.')

            if mes_inicial in mes_31 and 1 <= dia_inicial <= 31:
                break
            else:
                if mes_inicial in mes_31:
                    if dia_inicial > 31:
                        print(f'O mês escolhido possui apenas 31 dias, tente novamente.')
                    if dia_inicial < 0:
                        print('Dias Negativos não são permitidos, tente novamente.')
                    if dia_inicial == 0:
                        print('0 não é um dia permitido, tente novamente.')

        # Para Caso o Ano Não Seja Bissexto...
        else:
            if mes_inicial in mes_28_29 and 1 <= dia_inicial <= 28:
                break
            else:
                if mes_inicial in mes_28_29:
                    if dia_inicial > 28:
                        print(
                            f'{ano_inicial} não é um ano bissexto, logo Fevereiro possui apenas 28 dias, tente novamente.')
                    if dia_inicial < 0:
                        print('Dias Negativos não são permitidos, tente novamente.')
                    if dia_inicial == 0:
                        print('0 não é um dia permitido, tente novamente.')
            if mes_inicial in mes_30 and 1 <= dia_inicial <= 30:
                break
            else:
                if mes_inicial in mes_30:
                    if dia_inicial > 30:
                        print(f'O mês escolhido possui apenas 30 dias, tente novamente.')
                    if dia_inicial < 0:
                        print('Dias Negativos não são permitidos, tente novamente.')
                    if dia_inicial == 0:
                        print('0 não é um dia permitido, tente novamente.')
            if mes_inicial in mes_31 and 1 <= dia_inicial <= 31:
                break
            else:
                if mes_inicial in mes_31:
                    if dia_inicial > 31:
                        print(f'O mês escolhido possui apenas 31 dias, tente novamente.')
                    if dia_inicial < 0:
                        print('Dias Negativos não são permitidos, tente novamente.')
                    if dia_inicial == 0:
                        print('0 não é um dia permitido, tente novamente.')

    apart('Digite a Data Final')

    while True:  # Validar o Ano Final...
        ano_final = int(input('> Ano: '))
        if 3000 >= ano_final >= 1601:
            break
        else:
            if ano_final <= 1600:
                print('Ano Inválido (Anos abaixo de 1501 não são permitidos).')
            if ano_final >= 3001:
                print('Ano Inválido (Anos acima de 2500 não são permitidos).')

    while True:  # Validar o Mês Final...
        mes_final = str(input('> Mês: ')).strip().capitalize()
        if mes_final in mes_28_29 or mes_final in mes_30 or mes_final in mes_31:
            break
        else:
            print('Mês inválido,tente novamente.')

    while True:  # Validar o Dia Final...
        dia_final = int(input('> Dia: '))

        # Para Caso o Ano Seja Bissexto...
        if bissexto(ano_final):
            if mes_final in mes_28_29 and 1 <= dia_final <= 29:
                break
            else:
                if mes_final in mes_28_29:
                    if dia_final > 29:
                        print(f'{ano_final} é um ano bissexto, logo Fevereiro possui apenas 29 dias, tente novamente.')
                    if dia_final < 0:
                        print('Dias Negativos não são permitidos, tente novamente.')
                    if dia_final == 0:
                        print('0 não é um dia permitido, tente novamente.')

            if mes_final in mes_30 and 1 <= dia_final <= 30:
                break
            else:
                if mes_final in mes_30:
                    if dia_final > 30:
                        print(f'O mês escolhido possui apenas 30 dias, tente novamente.')
                    if dia_final < 0:
                        print('Dias Negativos não são permitidos, tente novamente.')
                    if dia_final == 0:
                        print('0 não é um dia permitido, tente novamente.')
            if mes_final in mes_31 and 1 <= dia_final <= 31:
                break
            else:
                if mes_final in mes_31:
                    if dia_final > 31:
                        print(f'O mês escolhido possui apenas 31 dias, tente novamente.')
                    if dia_final < 0:
                        print('Dias Negativos não são permitidos, tente novamente.')
                    if dia_final == 0:
                        print('0 não é um dia permitido, tente novamente.')

        # Para Caso o Ano Não Seja Bissexto...
        else:
            if mes_final in mes_28_29 and 1 <= dia_final <= 28:
                break
            else:
                if mes_final in mes_28_29:
                    if dia_final > 28:
                        print(f'{ano_final} não é um ano bissexto, logo Fevereiro possui apenas 28 dias, tente novamente.')
                    if dia_final < 0:
                        print('Dias Negativos não são permitidos, tente novamente.')
                    if dia_final == 0:
                        print('0 não é um dia permitido, tente novamente.')
            if mes_final in mes_30 and 1 <= dia_final <= 30:
                break
            else:
                if mes_final in mes_30:
                    if dia_final > 30:
                        print(f'O mês escolhido possui apenas 30 dias, tente novamente.')
                    if dia_final < 0:
                        print('Dias Negativos não são permitidos, tente novamente.')
                    if dia_final == 0:
                        print('0 não é um dia permitido, tente novamente.')
            if mes_final in mes_31 and 1 <= dia_final <= 31:
                break
            else:
                if mes_final in mes_31:
                    if dia_final > 31:
                        print(f'O mês escolhido possui apenas 31 dias, tente novamente.')
                    if dia_final < 0:
                        print('Dias Negativos não são permitidos, tente novamente.')
                    if dia_final == 0:
                        print('0 não é um dia permitido, tente novamente.')

    nome_mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
                'Novembro', 'Dezembro']
    num_mes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

    # Passar o mês de str para int...
    if mes_inicial in num_mes:
        mes_inicial = int(mes_inicial)
    if mes_final in num_mes:
        mes_final = int(mes_final)

    # Atribuir o nome do mês ao número dele...
    if mes_inicial in nome_mes:
        mes_inicial = nome_mes.index(mes_inicial)
        mes_inicial += 1
    if mes_final in nome_mes:
        mes_final = nome_mes.index(mes_final)
        mes_final += 1

    # Dias que faltam para o mês incial terminar...
    i = dia_inicial
    cont_dias = 0

    # Caso as datas fornecidas sejam iguais...
    if (ano_inicial == ano_final) and (mes_inicial == mes_final) and (dia_inicial == dia_final):
        apart('As datas fornecidas são iguais.')

    else:
        if mes_inicial in mes_28_29:

            # (Caso o ano inicial seja Bissexto)
            if bissexto(ano_inicial):
                for i in range(i, 29):
                    cont_dias += 1

            # (Caso o ano inicial não seja Bissexto)
            else:
                for i in range(i, 28):
                    cont_dias += 1

        if mes_inicial in mes_30:
            for i in range(i, 30):
                cont_dias += 1
        if mes_inicial in mes_31:
            for i in range(i, 31):
                cont_dias += 1

        prox_mes = mes_inicial + 1  # Passar para o próximo mês...

        # Caso os anos dados sejam iguais...
        if ano_inicial == ano_final:

            # Em quanto o próximo mês for menor que o mês final, somam-se os dias deste mês...
            while prox_mes < mes_final:
                if prox_mes in mes_28_29:
                    if bissexto(ano_inicial):
                        cont_dias += 29
                    else:
                        cont_dias += 28
                if prox_mes in mes_30:
                    cont_dias += 30
                if prox_mes in mes_31:
                    cont_dias += 31
                prox_mes += 1

            # Quando o próximo mês for igual ao mês final, soma-se apenas os dias deste mês...
            if prox_mes == mes_final:
                cont_dias += dia_final

        # Caso os anos dados sejam diferentes...
        if ano_inicial != ano_final:

            # Em quanto o próximo mês for menor que 12 (Último mês do ano), somam-se os dias para acabar o ano...
            while prox_mes <= 12:
                if prox_mes in mes_28_29:
                    if bissexto(ano_inicial):
                        cont_dias += 29
                    else:
                        cont_dias += 28
                if prox_mes in mes_30:
                    cont_dias += 30
                if prox_mes in mes_31:
                    cont_dias += 31
                prox_mes += 1

        prox_ano = ano_inicial + 1  # Passar para o próximo ano...

        # Em quanto o próximo ano for menor que o ano final, somam-se os dias para acabar ano...
        while prox_ano < ano_final:
            prox_mes = 1
            while prox_mes <= 12:
                if prox_mes in mes_28_29:
                    if bissexto(prox_ano):
                        cont_dias += 29
                    else:
                        cont_dias += 28
                if prox_mes in mes_30:
                    cont_dias += 30
                if prox_mes in mes_31:
                    cont_dias += 31
                prox_mes += 1
            prox_ano += 1

        # Quando o próximo ano for igual ao ano final...
        if prox_ano == ano_final:
            prox_mes = 1  # (Próximo mês passa a valer Janeiro)

            # Em quanto o próximo mês for menor que o mês final, somam-se os dias...
            while prox_mes < mes_final:
                if prox_mes in mes_28_29:
                    if bissexto(prox_ano):
                        cont_dias += 29
                    else:
                        cont_dias += 28
                if prox_mes in mes_30:
                    cont_dias += 30
                if prox_mes in mes_31:
                    cont_dias += 31
                prox_mes += 1

            # Quando o próximo mês for igual ao mês final, somam-se os dias desse mês...
            if prox_mes == mes_final:
                cont_dias += dia_final

        apart(f'Entre as datas há {cont_dias} dias')


if __name__ == '__main__':
    main()
