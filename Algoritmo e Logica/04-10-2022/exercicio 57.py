n = int(input("digite um numero "))
s = 0
x = 2
so = 0
for y in range(1, n+1):
    s = 1/x**x
    so += s
    x += 1
s = so + 1
print(f'com N valendo {n} o S vale {s:.{n}f}')