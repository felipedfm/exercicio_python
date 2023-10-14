p1 = 5000000
p2 = 7000000
ano = 0
while p2 > p1:
    p1 = p1 + (p1*0.03)
    p2 = p2 + (p2*0.02)
    ano += 1
print(f'serão nescessarios {ano} anos para o pais A alcançar o pais B')