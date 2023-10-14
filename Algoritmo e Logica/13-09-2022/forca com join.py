print('-='*20)
print('         JOGO DA FORÇA')
print('-='*20)
import random
 
palavra = random.choice(["apple", "banana", "cherry"])
palavra_lista = []
tentativas = 0
print(palavra)
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
        print("perdeu")
        break
if tentativas < 5 : 
    print("Voce descobriu a palavra!")


