n = int(input("digite um numero "))
to = 0
for c in range(1, n + 1):
    if n % c == 0:
        to += 1
if to == 2:
    print("é primo")
else:
    print("não é primo")
