Q1, Q2, Q3 = [int(x) for x in input().split()]
E1, E2, E3 = [int(x) for x in input().split()]
V = ((Q1+Q2+Q3)-((E1+E2+E3)*2 + (E1+E2+E3))) 
print(V)