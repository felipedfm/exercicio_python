repete = 1
while (repete == 1):
    import random
    n = random.randint(1,6)
    print(n)
    x = input("deseja continuar S/N??").strip().capitalize()
    if (x == "s"):
         repete = 1
