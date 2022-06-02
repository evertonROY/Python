N = int(input())
final = []
lista = [int(y) for y in input().split()]
C = int(input())
for i in range(N):
    Vf = lista[i]
    Vf = Vf*C
    final = final + [Vf]
print(*final, sep=' ')