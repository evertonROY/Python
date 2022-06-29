N = int(input())
B = [int(x) for x in input().split()]
esfera = [y for y in B if y<= 7]

lista_zeros = [0] * 8

for i in esfera:
  lista_zeros[i] = i
ordem = [c for c in lista_zeros if c != 0]
print(*ordem, sep=' ')
if len(ordem) == 7:
  print("Saia Shenlong e realize o meu desejo")
else:
  print("Nao encontramos todas")


