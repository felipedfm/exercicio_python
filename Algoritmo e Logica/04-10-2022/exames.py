i = int(input("digite a nota do primeiro exame de 0 á 100"))
ii = int(input("digite a nota do segundo exame de 0 á 100"))
iii = int(input("digite a nota do terceiro exame de 0 á 100"))
iv = int(input("digite a nota do quarto exame de 0 á 100"))
v = int(input("digite a nota do quinto exame de 0 á 100"))
me = 70
if i >= me and ii >= me and iii >= me and iv >= me and v >= me:
    print("sua classificação é rank A")
elif i>= me and ii >= me and iv >= me and iii >= me:
    if v < me:
        print("sua classificação é rank B")
elif i>= me and ii >= me and iv >= me and v >= me:
    if iii < me:
        print("sua classificação é rank B")
elif i >= me and ii >= me and iii >= me:
    if iv < me and iv < me:
         print("sua classificação é rank C")
elif i >= me and ii >= me and iv >= me:
    if iii < me and v < me:
        print("sua classificação é rank C")
else:
    print("Reprovado")