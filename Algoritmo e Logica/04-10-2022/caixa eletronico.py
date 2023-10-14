va = int(input("quanto deseja sacar? "))
tot = va
notas = 100
tnotas = 0
while True:
    if tot >= notas:
        tot -= notas
        tnotas += 1
    else:
        if tnotas > 0:
            print(f'{tnotas} notas de R${notas}')
        if notas == 100:
            notas = 50
        elif notas == 50:
            notas = 20
        elif notas == 20:
            notas = 10
        elif notas == 10:
            notas = 5
        elif notas == 5:
            notas = 1
        tnotas = 0
        if tot == 0:
            print(f'total sacado de {va}')
            break
