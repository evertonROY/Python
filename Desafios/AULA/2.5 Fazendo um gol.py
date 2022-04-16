Z, G = input().split()
D, C = input().split()

if Z != D:
    print("Bloqueado")
elif Z == D:
    print("Driblado")

if Z != D:
    print()
elif G == C :
    print("Gol")
else:
    print("...e o goleiro pega")