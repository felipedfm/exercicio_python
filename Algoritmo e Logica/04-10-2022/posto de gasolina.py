litros = float(input("Digite quantos litros você quer abastecer: "))
combustivel = input("Digite A para álcool ou G para gasolina: ")
preco = 0
if combustivel == "A" or combustivel == "a":
    preco = litros * 1.9
    if litros <= 25:
        preco -= 1.9 * litros * 0.02
    else:
        preco -= 1.9 * litros * 0.04
elif combustivel == "G" or combustivel == "g":
    preco = litros * 2.7
    if litros <= 25:
        preco -= 2.7 * litros * 0.03
    else:
        preco -= 2.7 * litros * 0.05
print(f"O preço a pagar é R${preco:.2f}")