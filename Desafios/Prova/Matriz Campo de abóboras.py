N = int(input())
B = 0
C = 0
X = []

for i in range(N):
    q = [int(h) for h in input().split()]
    X.append(q)

H, R = [int(h) for h in input().split()]

for i in range(N):
    B += X[H][i]
    C += X[i][R] 

if H > R:
    C -= X[H][R]
else:
    B -= X[H][R]

print("Harry", B)
print("Ron", C)
