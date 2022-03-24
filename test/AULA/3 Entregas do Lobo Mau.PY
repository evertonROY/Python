#T = ('tamanho')   #60     100
#D = ('distancia') #20     51
#V = ('KM')        #1$     2$ 
#P = ('pedagio')   #10$    50$      
                  #90     250

T, D = [int(x) for x in input().split()]
V, P = [int(x) for x in input().split()]
F = int(T*V+(int(T/D)*P))
print(F)

'''T, D = input().split()
V, P = input().split()
T = int(T)
D = int(D)
V = int(V)
P = int(P)
F = int(T*V+(int(T/D)*P))
print(F)'''

