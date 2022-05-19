N = int(input())
for i in range(N + 1):
    if i != 0:
        B = i % 5
        if B == 0:
            print(i)
