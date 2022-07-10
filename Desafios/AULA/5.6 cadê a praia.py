m=[] 

for z in range(10): 

    l=input().split() 

    m.append(l) 

for i in range(10): 

    for j in range(10): 

        if m[i][j] == 't' and i!=0: 

            if m[i-1][j]=='*': 

                m[i][j]='p' 

for q in range(10): 

    for w in range(10): 

        if m[q][w] == 't' and w!=0: 

            if m[q][w-1]=='*': 

                m[q][w]='p' 

for e in range(10): 

    for r in range(10): 

        if m[e][r] == 't' and e!=9: 

            if m[e+1][r]=='*': 

                m[e][r]='p' 

for a in range(10): 

    for b in range(10): 

        if m[a][b] == 't' and b!=9: 

            if m[a][b+1]=='*': 

                m[a][b]='p' 
for x in range(10): 
    for y in range(10): 
        if y!=9: 
            print(m[x][y],"",end="") 
        else: 
            print(m[x][y])