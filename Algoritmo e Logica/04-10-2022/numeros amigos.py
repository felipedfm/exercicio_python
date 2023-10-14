n1 = int(input("digite o primeiro numero "))
n2 = int(input("digite o segundo numero "))
x = 1
so = 0
while x < n1:
    if n1 % x == 0:
        so += x
    x += 1
if so == n2:
    print("são amigos")
else:
    print("não são amigos")
