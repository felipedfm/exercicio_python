lista = []
on = True
while on:
    def chama():
    

        for y in range (4):
            x= int (input("digite uma valor"))
            lista.append(x)
        
                
                
    chama()
    print ("a média é", sum(lista)/len(lista))
    
    cont = (input("dejesa continuar?")).strip()       
    if cont != "s":
        on = False

