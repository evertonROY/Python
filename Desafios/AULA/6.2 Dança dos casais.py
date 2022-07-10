N=int(input()) 

v=[int(x) for x in input().split()] 

u=[int(x) for x in input().split()] 

cont = 0 

v.sort(reverse = True) 

u.sort() 

 

for i in v: 

    print(v[cont], u[cont]) 

    cont = cont + 1 