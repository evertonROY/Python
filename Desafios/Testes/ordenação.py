# 4 2 1 3 em 1 2 3 4
P = [int(x) for x in input().split()] 
H = len(P)


for fr in range(H - 1, 0, -1):
    maior = 0
    for y in range(1, fr + 1):
        if P[y] < P[maior]:
            maior = y
    P[fr], P[maior] = P[maior], P[fr]

print(P)