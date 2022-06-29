N = int(input())
U = [int(x) for x in input().split()]
V = [int(x) for x in input().split()]
D = [int(x) for x in input().split()]
PO = False
for i in range(N):
    if U[i] + V[i] == D[i]:
        PO = True
if PO:
    print("OK")
else:
    print("NOPE :(")