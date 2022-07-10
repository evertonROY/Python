from operator import itemgetter 

N, Q = input().split() 

N = int(N) 

Q = int(Q) 

n = 0 

matriz1 = [] 

matriz2 = [] 

lista = [] 

lista_ordenada = [] 

for i in range(Q): 

    linha = [int(x) for x in input().split()] 

    matriz1.append(linha) 

for linha in matriz1: 

    lista.append(linha) 

lista_ordenada = sorted(lista, key=itemgetter(0), reverse=True) 

for i in range(len(lista_ordenada)): 

    if i+1 in range(len(lista_ordenada)) and lista_ordenada[i][0] == lista_ordenada[i+1][0]: 

        if lista_ordenada[i][1] > lista_ordenada[i+1][1]: 

            maior = lista_ordenada[i] 

            lista_ordenada[i] = lista_ordenada[i+1]  

            lista_ordenada[i+1] = maior          

C = int(input()) 

for i in range(C): 

    linha = [int(x) for x in input().split()] 

    matriz2.append(linha) 

n = len(matriz1) 

esq = 0 

dir = n - 1 

for elem in matriz2: 

    v = lista_ordenada 

    n = len(matriz1) 

    esq = 0 

    dir = n - 1 

    while esq <= dir: 

        meio = (esq + dir) // 2 

        if v[meio][0] == elem[0] and v[meio][1] == elem[1]: 

            break 

        elif v[meio][0] < elem[0]: 

            dir = meio - 1        

        else: 

            esq = meio + 1   

    if meio < N: 

        print("Sim") 

    else: 

        print("Nao")