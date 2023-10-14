print('-='*20)
print('         JOGO DA FORÇA')
print('-='*20)
teste = str(input("digite um palavra"))
palavra =[""]
y = len(teste)
print (y)
repete = True
for x in range (0,y,1):
    palavra.append("_")
   
print(palavra)
while repete:
    letra = input("digite uma letra")

    for x in teste:
        if x == letra:
            palavra.append(letra)
            print ("acertou")
            print (palavra)
            y = y - 1
            print(y)

