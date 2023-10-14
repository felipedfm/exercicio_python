n = int(input("Digite um numero "))
a=0
b=1
c=2
d=0
while d < n:
    a += 1
    b += 1
    c += 1
    d = a * b * c
if d == n:
    print("Esse numero é triangular")
else:
    print("Esse numero nao é triangular")