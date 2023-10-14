dec = int(input("digite um numero decimal até 32"))
bi = []
quo = 1    
if dec > 0 and dec < 32:    
    while quo >= 1:
        res = dec%2
        bi.insert(0,res)
        quo = dec//2
        dec = quo
    print(bi)
else:
    print("voce digitou um numero invalido")

