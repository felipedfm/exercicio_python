
n1 = int(input("digite um numero inteiro positivo para ser o dividendo: "))
n2 = int(input("digite um numero inteiro positivo para ser o divisor: "))
quo = 0
x = n1
while x >= n2:
    x = x - n2
    quo += 1
print(f"{n1} / {n2} = {quo} ")
