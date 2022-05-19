T = int(input())
D = int(input())
P = (0)
while D != 0:
    if D > P:
        P = D
        D = int(input())
    else:
        D = int(input())
if P > T:
    print("ALARME")
else:
    print("O Havai pode dormir tranquilo")
