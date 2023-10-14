n1 = float(input("digite o primeiro numero"))
n2 = float(input("digite o segundo numero"))
n3 = float(input("digite o terceiro numero"))
lis = [n1, n2, n3]
nm = max(lis)
lis.remove(max(lis))
nm = nm*5
np1 = lis[0]*2.5
np2 = lis[1]*2.5
mp = (nm + np1 + np2)/10
print(f'a media ponderada é {mp}')
