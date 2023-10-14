n = int(input("Digite o enesimo termo"))
fa = 1
i = 1
e = [1]
while i <= n:
    fa = fa * i
    df = 1 / fa
    pe = df
    e.append(pe)
    i += 1
    if fa < 10000000000000000:
        print(f"o valor de {i - 1} ! {fa} ")
    else:
        print(f'o valor de {i -1 } ! {fa:.16e}')
    print(f'o valor de Euler é  {sum(e)}\n')