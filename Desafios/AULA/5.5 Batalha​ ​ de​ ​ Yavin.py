a,b=input().split() 
a=int(a) 
b=int(b) 
m1=[] 
m2=[] 
p=0 
for i in range(a): 

  l=[int(c) for c in input().split()] 

  m1.append(l) 

for j in range(b): 

  l2=[int(d) for d in input().split()] 

  m2.append(l2) 

for k in range(b): 

  for x in range(m2[k][0]): 

    if m1[m2[k][0]-1-x][m2[k][1]]==1: 

      p+=1 

      m1[m2[k][0]-1-x][m2[k][1]]=0 

      break 

    else: 

      continue 

print(p)