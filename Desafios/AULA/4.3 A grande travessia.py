S, N = map(int, input().split())
L = [0]*N
for i in range(0, S):
    P = int(input())
    for n in range(0, N, P):
        L[n] = 1
for L in L:
    print(L,end=" ")