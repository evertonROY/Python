N = int(input())

C = int(N%3)
V = int(N%3)
L = int(N%3)

if N%3 == 1:
    print(C + 1)
elif N%3 == 2:
    print(C + 1 & V + 1)
else: 
    print("opa") 




