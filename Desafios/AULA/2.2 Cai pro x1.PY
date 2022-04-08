
LA, PA = [int(x) for x in input().split()]
LB, PB = [int(x) for x in input().split()]
LC, PC = [int(x) for x in input().split()]

if LA + LB + LC > PA + PB + PC:
    print("Lucas")
elif LA + LB + LC == PA + PB + PC:
    print("Empate")
else:
    print("Pedro")

