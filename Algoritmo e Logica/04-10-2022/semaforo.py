distsema = float ( input("digite a distancia entre os semaforos em metros "))
velocimax = float (input("digite a velocidade maxima da via"))
acelera = float (input("digite aceleração média dos carros em metros por sugundo "))

convervelomax = velocimax/3.6
tempoace = convervelomax/acelera
tempsema = distsema/convervelomax
tempototal = (tempoace+tempsema)-3
print (tempototal)

