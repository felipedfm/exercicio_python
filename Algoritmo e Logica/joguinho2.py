repete = 1
while (repete == 1):
    import random
    n = random.randint(1,6)
    nun= int(input("escolha um numero de 1 a 6"))
    if ( nun == n):
        print("acertou")
    else:
        print ("errou o numero é" , n )
    x = input("deseja continuar S/N??").strip().capitalize()
    if (x == "s"):
         repete = 1
