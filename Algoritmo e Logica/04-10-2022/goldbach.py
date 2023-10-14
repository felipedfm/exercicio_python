def sp(n):
  pri = 1
  for i in range (2,int(n/2),1):
    if(n % i == 0):
        pri = 0
        break
  return pri

n = int(input("digite um numero : "))

f = 0
i = 2
for i in range (2,int(n/2),1):
  if(sp(i) == 1):
    if(sp(n-i) == 1):
        print(n,"pode ser expresso como a soma de",i,"e",n-i)
        f = 1;
if (f == 0):
  print(n,"não pode ser expresso como a soma de dois primos")