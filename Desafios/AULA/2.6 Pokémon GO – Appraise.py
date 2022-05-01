#A, D, P = [int(x) for x in input().split()]
A, D, P = map(int, input().split())
V = float(A + D + P)
if V <= float((50*110)/100):
    print("Seu pokemon nao fara progresso em batalhas")
elif V <= float((66*110)/100):
    print("Seu pokemon esta acima da media")
elif V <= float((79*110)/100):
    print("Seu pokemon certamente me chamou atencao")
elif V <= 110:
    print("Seu pokemon e uma maravilha")
else:
    print("Hum, parece que houve um erro")



