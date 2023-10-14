pra = int(input("digite o numero correspondente a praga que gostaria de combater\n 1: Ervas daninhas \n 2: gafanhotos \n 3: broca\n 4: todos acima \n "))
are = float(input("digite o tamanho da area a ser pulverizada em acres"))
val = 1
desa = 1
desv = 1
vd = 0
if pra == 1:
    val = 50
    val = val*are
    if are >= 1000:
        desa = 0.05
    if val >= 750:
        desv = 0.1
        vd = val - 750
    vt = val-(val*desa)
    vt = val-(vd*desv)
    print(f'a valor total a ser pago é R${vt:.2f}')
elif pra == 2:
    val = 100
    val = val*are
    if are >= 1000:
        desa = 0.05
    if val >= 750:
        desv = 0.1
        vd = val - 750
    vt = val-(val*desa)
    vt = val-(vd*desv)
    print(f'a valor total a ser pago é R${vt:.2f}')
elif pra == 3:
    val = 150
    val = val*are
    if are >= 1000:
        desa = 0.05
    if val >= 750:
        desv = 0.1
        vd = val - 750
    vt = val-(val*desa)
    vt = val-(vd*desv)
    print(f'a valor total a ser pago é R${vt:.2f}')
elif pra == 4:
    val = 250
    val = val*are
    if are >= 1000:
        desa = 0.05
    if val >= 750:
        desv = 0.1
        vd = val - 750
    vt = val-(val*desa)
    vt = val-(vd*desv)
    print(f'a valor total a ser pago é R${vt:.2f}')
else:
    print("numero não está relacionado a nenhuma praga")