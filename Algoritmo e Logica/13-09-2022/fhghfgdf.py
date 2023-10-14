import random
mylist = ["apple", "banana", "cherry"]

while True:
    print(random.choice(mylist))
    ok = str(input(" sim ou nao : ")).strip().lower()
    if ok == "n" or "nao":
        break
    
    
    
