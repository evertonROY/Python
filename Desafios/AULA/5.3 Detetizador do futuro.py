H, G = map(int, input().split())
P1 = [[int(x) for x in input().split()] for i in range(H)]
B = int(input())
X = 0
for i in range(B):
    M, N = map(int, input().split())
    if P1[M- 1][N - 1] == 1:
        P1[M - 1][N - 1] -= 1
for l in range(H):
    for c in range(G):
       if P1[l][c] == 1:
           X += 1
if X == 0:
    print("HASTA LA VISTA BABY")
else:
    print("ILL BE BACK")