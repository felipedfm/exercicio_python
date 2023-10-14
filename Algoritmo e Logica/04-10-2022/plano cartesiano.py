x = int(input("digite a coordenada do eixo X"))
y = int(input("digite a coordenada do eixo y"))
if x > 0 and y > 0:
    print("o ponto pertence ao primeiro quadrante")
elif x < 0 and y > 0:
    print("o ponto pertence ao segundo quadrante")
elif x < 0 and y < 0:
    print("o ponto pertence ao terceiro quadrante")
elif x > 0 and y < 0:
    print("o ponto pertence ao quarto quadrante")
else:
    print("o ponto pertence ao eixo cartesiano")