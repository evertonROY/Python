A, D, P = [int(x) for x in input().split()]
#A, D, P = map(int, input().split())
V = int(A + D + P)
if V <= 50*110/100:
    print("Seu pokemon nao fara progresso em batalhas")
elif V <= 66*110/100:
    print("Seu pokemon esta acima da media")
elif V <= 79*110/100:
    print("Seu pokemon certamente me chamou atencao")
else:
    print("Hum, parece que houve um erro")

print(V)

