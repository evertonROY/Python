A = int(input())
B = map(int, input().split())
par = []
impar = []
for i in B:
    if i%2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(*par, sep=" ")
print(*impar, sep=" ")
