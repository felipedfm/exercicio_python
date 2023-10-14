le = input("digite uma letra")
le = le.lower()
vo = ["a", "e", "i", "o", "u"]
if le in vo:
    print(f" a letra {le.upper()} é uma vogal ")
else:
    print(f" a letra {le.upper()} é uma consoante ")