repete = True
while (repete):
    nota1 = int(input("digite a nota"))
    nota2 = int(input("digite a nota"))
    media = (nota1 + nota2)/2
    print ("media=" + str (media))
    if (media >=7):
           print("vc passou")
    else:
            print ('vc não passou')
            
    x = input("deseja continuar S/N??")
    if (x == "N"):
        repete = False
