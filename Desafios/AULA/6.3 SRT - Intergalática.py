N = int(input()) 

i = [] 

r = [] 

for j in range(N): 

    I, R = [int(x) for x in input().split()] 

    i.append(I) 

    r.append(R) 

 

for j in range(N-1,0,-1): 

     for n in range (0, j): 

          if r[n] < r[n + 1]: 

               r[n], r[n+1] = r[n+1], r[n] 

               i[n], i[n+1] = i[n+1], i[n] 

                

for j in range(N): 

     print(i[j],r[j])