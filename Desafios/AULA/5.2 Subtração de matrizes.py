L, C = [int(x) for x in input().split()]
A=[]
B=[]


for i in range(L):
  linha = [int(x) for x in input().split()]
  A.append(linha)


for i in range (L):
  linha = [int(x) for x in input().split()]
  B.append(linha)


for i in range(L):
  for x in range(C):
    A[i][x] -= B[i][x]
    print(A[i][x],end=" ")
  print()