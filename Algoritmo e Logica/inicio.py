nome ="inicio"
veio = ""
idveio = -2
while (nome != "fim" and"Fim"):
    nome = input("digite o nome do aluno ou fim")
    if (nome != "fim" and "Fim"):
       idade = int(input("qual sua idade?"))
       if (idade >= idveio):
        veio = nome
        idveio = idade
print ("o aluno mais velho é" + veio)
print ("a idade do mais velho é" + str(idveio))
    
