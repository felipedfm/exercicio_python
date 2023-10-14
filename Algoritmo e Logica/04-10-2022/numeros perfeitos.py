n1 = int(input("digite o primeiro numero "))
x = 1
so = 0
for y in range(1, n1):
    if n1 % x == 0:
        so += x
    x += 1
if so == n1:
    print("é perfeito")
else:
    print("não é perfeito")
