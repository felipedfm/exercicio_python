dn = int(input("digite o numero de 1 á 7 "))
dia = {1: "Domingo",2: "segunda",3: "terça",4: "quarta", 5: "quinta", 6: "sexta",7: "sabado" }
if dn in dia:
   print(dia[dn])
else:
   print('numero invalido')