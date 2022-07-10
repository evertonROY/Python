N, M = [int(n) for n in input().split()]

matriz = []

for i in range(N):

    linha = [int(n) for n in input().split()]

    matriz.append(linha)

ovos = 0

for i in range(N):

    if (i == 0 or i % 2 == 0):

        for h in range(M):

            ovos = ovos + matriz[i][h]

            if ovos < 0:

                ovos = 0

    else:

        for h in range(M):

            ovos = ovos + matriz[i][M - 1 - h]

            if ovos < 0:

                ovos = 0

print(ovos)
