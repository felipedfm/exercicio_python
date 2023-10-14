sa = float(input("digite o valor do salario"))
des = sa*0.11
if des >= 324.29:
    print("o desconto vai ser de R$324,29")
else:
    print(f"o desconto vai ser de R${des}")