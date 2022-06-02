EUcomp = 0
ELEcomp = 0

N = int(input())
cartas = [int(y) for y in input().split()]
R = int(input())

for i in range(R):
    Xi, Yi = [int(x) for x in input().split()]
    if cartas[Xi -1] > cartas[Yi -1]:
        EUcomp+=1
    elif cartas[Xi -1] < cartas[Yi -1]:
        ELEcomp+=1

if EUcomp > ELEcomp:
    print("Venci")
elif EUcomp < ELEcomp:
    print("Perdi")
else:
    print("Empatou")