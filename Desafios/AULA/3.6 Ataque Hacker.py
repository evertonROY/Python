A, B = map(int, input().split())
T = 0
G = 0
for i in range(A, B + 1):
    for n in range(2, i):
        if i%n == 0:
            T += 1
    if T == 0:
        G += 1
    else:
       T = 0
print(G)