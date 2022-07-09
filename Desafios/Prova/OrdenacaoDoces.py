# V = int(input())
# L = [int(x) for x in input().split()] 
# C = []
# P = []
# N = len(L)
# H = len(P)
# for fim in range(N - 1, 0, -1):
#     maior = 0
#     for i in range(1, fim + 1):
#         if L[i] > L[maior]:
#             maior = i
#     L[fim], L[maior] = L[maior], L[fim]
# for i in range(V):
#     if L[i]%2 == 0:
#         P.append(L[i])      
#     else:
#         C.append(L[i])
# H = len(P)
# for fr in range(H - 1, 0, -1):
#     maior = 0
#     for y in range(1, fr + 1):
#         if P[y] < P[maior]:
#             maior = y
#     P[fr], P[maior] = P[maior], P[fr]
# print(*C, *P, sep=" ")
