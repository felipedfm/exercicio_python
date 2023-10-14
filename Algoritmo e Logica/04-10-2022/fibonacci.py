n = int(input("digite um numero"))
f1 = 0
f2 = 1
con = 2
print(f1)
print(f2)
while con < n:
    f3 = f1 + f2
    print(f3)
    f1 = f2
    f2 = f3
    con+=1
