N=int(input()) 

v=[int(x) for x in input().split()] 

u=[int(x) for x in input().split()] 

vL = len(v) 

v.sort() 

 

for elem in u: 

    esq = 0 

    dir = vL - 1 

    if elem == 0: 

        break 

    while esq <= dir: 

        meio = (esq + dir) // 2 

        if v[meio] == elem: 

            break 

        elif elem < v[meio]: 

            dir = meio - 1 

        else: 

            esq = meio + 1 

 

    if v[meio] == elem: 

        print(meio) 

    else: 

        print("Nao foi visitado ainda.")