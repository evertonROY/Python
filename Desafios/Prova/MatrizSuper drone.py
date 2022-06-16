N = int(input())
B = 0
X = []

for i in range(N):
    q = [int(h) for h in input().split()]
    X.append(q)

C = int(input())

for i in range(C):
    L, C = map(int, input().split())
    B = B+X[L][C]
    
print(B)  