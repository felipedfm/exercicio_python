n1 = int(input("Informe o valor de n1"))
n2 = int(input("Informe o valor de n2"))
n3 = int(input("Informe o valor de vezes"))
serie = 0
print(n1, end=", ")
print(n2, end=", ")
for i in range(3, n3):
    if (i % 2 == 0):
        serie = n2 - n1
    else:
        serie = n2 + n1

    n1 = n2
    n2 = serie

    print(serie, end=", ")