#Um determinado material radioativo perde metade de sua massa a cada 50 segundos. Dada
#a massa inicial, em gramas, fazer um programa que calcule o tempo necessário para
#que essa massa se torne menor que 0,5 grama. O programa deve escrever a massa
#inicial, a massa final e o tempo calculado em horas, minutos e segundos.

mass_inicial = float(input('Digite a Massa do Material (gramas): '))
if mass_inicial < 0.5:
    print('A massa dada já é menor que 0,5 gramas.')
else:
    mass_final = mass_inicial
    tot_temp = 0
    while mass_final >= 0.5:
        mass_final = mass_final / 2
        tot_temp += 50
        temp2 = tot_temp
    print(f'A massa inicial do material foi de {mass_inicial} gramas')
    print(f'A massa final do materia foi de {mass_final} gramas')
    if tot_temp > 0:
        print(f'Para que a massa do material ficasse menor que 0,5 gramas, levou: ')
    temp_hr = tot_temp // 3600
    tot_temp %= 3600
    temp_min = tot_temp // 60
    tot_temp %= 60
    temp_seg = tot_temp // 1
    if temp_hr >= 1:
        print(f'{temp_hr} Horas,', end='')
    if temp_min >= 1:
        print(f'{temp_min} Minutos e {temp_seg} Segundos', end='')
    if temp2 // 60 < 1:
        print(f'{temp2} Segundos.')
