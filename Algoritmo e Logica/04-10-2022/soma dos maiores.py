n1 = int(input("digite o primeiro numero"))
n2 = int(input("digite o segundo numero"))
n3 = int(input("digite o terceiro numero"))
l = [n1, n2, n3]
m1 = max(l)
l.remove(max(l))
m2 = max(l)
print(f'{m1} + {m2} = ', m1 + m2)