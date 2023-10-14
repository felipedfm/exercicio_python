vd = float(input("digite o valor que deseja emprestado"))
ren = float(input("digite o valor da sua renda"))
pre = int(input("em quantas vezes gostaria de dividir?"))
vp = vd/pre
lim = ren*10
limp = ren*0.3
if vd <= lim and vp <= limp:
    print("emprestimo aprovado")
elif vd > lim or vp > limp:
    print("emprestimo negado")
    if vd > lim and vp < limp:
        print("sua renda é insuficiente, tente um valor menor ")
    if vd < lim and vp > limp:
        print("as prestações estão muito altas para sua renda , tente um numero maior de parcelas")
