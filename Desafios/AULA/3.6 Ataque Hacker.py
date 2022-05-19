A, B = map(int, input().split())
P = 1
for i in range(A, B+1):
   C = P%i
   while C == 0:
       P += 1


   print(i, P)
    