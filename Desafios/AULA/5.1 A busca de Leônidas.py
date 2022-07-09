Q = 10
c = 10

A = input()
A = int(A)
O = False
matriz = []
for i in range(Q):
   linha = [int(x) for x in input().split()]
   matriz.append(linha)
   if A in linha: 
      O = True
if O:
    print("sim")
    
else:
  print("nao")