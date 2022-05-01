#A, D, P = [int(x) for x in input().split()]
A, D, P = map(int, input().split())
V = int(A + D + P)
PC = int((V*100)/110)
if PC <= 50:
    print("Seu pokemon nao fara progresso em batalhas")
elif PC <= 66:
    print("Seu pokemon esta acima da media")
elif PC <= 79:
    print("Seu pokemon certamente me chamou atencao")
elif PC <= 100:
    print("Seu pokemon e uma maravilha")
else:
    print("Hum, parece que houve um erro")
print(V, "é", V*100/110,"%","De 110")