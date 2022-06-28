v = [4, 2, 7, 6, 1]
n = len(v)

for fim in range(n - 1, 0, -1):
    imaior = 0
    for i in range(1, fim + 1,):
        if v[i] > v[imaior]:
            imaior = i
    v[imaior], v[fim] = v[fim], v[imaior] 

print(v)