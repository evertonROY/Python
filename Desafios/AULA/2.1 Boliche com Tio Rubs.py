'''
a = qtd pistas                    1
b = qtd pessoas por pistas        9
c = qtd alunos                    4
'''

A, B, C = [int(x) for x in input().split()]
 
if (A*B) > C:
    print("S")
else:
    print("N")    
