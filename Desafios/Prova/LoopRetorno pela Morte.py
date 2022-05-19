C = int(input())
G = 0
for i in range(C):
  L, M, T = map(int, input().split())
  D = L* M + T
  G = D + G
print(G)

