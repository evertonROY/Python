A, B, C = map(int, input().split())
if   A != B & B == C:
    print("A")
elif B != A & A == C:
    print("B")
elif C != A & A == B:
    print("C")
else:
    print("Empate")