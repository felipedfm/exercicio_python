ca = input("digite um caracter")
vo= ["a", "e", "i", "o", "u"]
if ca.isalpha():
    if ca in vo:
        print(f'{ca} é uma vogal')
    else:
        print(f'{ca} é uma consoante')
elif ca.isdecimal():
    print(f"{ca} é um numero")
else:
    print(f"{ca} é um simbolo")
