m=[]
co, d = map(int, input().split())
l=[]
morte=0
temp=0
for linha in range(c):
  l=list(input().split())[:c]
  m.append(l)
while d >0:
  d-=1
  x,y = map(int, input().split())
  for k in range(x, -1, -1):
    temp=m[k][y]
    if temp=='1': 
        morte +=1
        m[k][y]='0'
        break
print(morte)