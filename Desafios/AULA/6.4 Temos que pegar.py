Q, classificação, ordem = input().split() 

Q = int(Q) 

 

Nome = [] 

Nivel = [] 

for j in range(Q): 

    nome, nivel = input().split() 

    Nome.append(nome) 

    Nivel.append(int(nivel)) 

 

      

if classificação == 'N': 

     A = Nome 

     B = Nivel  

else: 

     B = Nome 

     A = Nivel 

      

if ordem == 'C': 

     for j in range(1, Q): 

          i = j 

          while i >= 1 and A[i] < A[i-1]: 

               A[i], A[i-1] = A[i-1], A[i] 

               B[i], B[i-1] = B[i-1], B[i] 

               i -= 1 

           

if ordem == 'D': 

     for j in range(1, Q): 

          i = j 

          while i >= 1 and A[i] > A[i-1]: 

               A[i], A[i-1] = A[i-1], A[i] 

               B[i], B[i-1] = B[i-1], B[i] 

               i -= 1 

 

if classificação == 'N': 

     for j in range(Q): 

          print(A[j],B[j]) 

else: 

     for j in range(Q): 

          print(B[j],A[j])