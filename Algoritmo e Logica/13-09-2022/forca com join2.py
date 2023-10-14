import time
print('-='*20)
print('         JOGO DA FORÇA')
print('-='*20)
import random
on = True
while (on): 
    palavra = random.choice(["carro", "gato", "mulher", "criança", "cachorro", "arvore", "cavalo", "elefante", "casa", "pedra", "geladeira", "luva", "chuva", "sorte", "morte", "vida", "palhaço", "comida", "amor", "planeta" "churrasco", "cerveja", "carne", "tigre", "floresta"  ])
    palavra_lista = []
    tentativas = 0
    print('escolhendo uma palavra')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    
    for x in range(0, len(palavra)):
        palavra_lista.append('_')

    print(' '.join(palavra_lista))

    letra = ('')
    while (''.join(palavra_lista) != palavra):
            letra = input("digite uma letra: ").strip().lower()
            pos = 0
           
                

            for x in palavra:
                if x == letra:
                    palavra_lista[pos] = x
                pos += 1
        

            if letra not in palavra:
                print("errouuu")
                tentativas += 1                
            print(' '.join(palavra_lista))
            if tentativas > 5:
                palavra_lista = palavra
            
      
    if tentativas < 5: 
            print("Voce descobriu a palavra!")
            cont = input("coninuar S/N").strip().lower()
    else:
        if tentativas > 5 :
            print("perdeuuu, a palavra certa era", palavra )
            
            cont = input("coninuar S/N").strip().lower()
   
       
    if cont == "n":
        print ('obrigado por jogar')
        on = False
       
