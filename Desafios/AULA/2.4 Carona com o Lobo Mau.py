import math
N = int(input())
if N%3 == 2:
    print("Chapeuzinho Vermelho",math.ceil(N/3))
    print("Vovozinha",math.ceil(N/3))
    print("Lobo Mau",math.ceil(N/3 - 1))
elif N%3 == 1:
    print("Chapeuzinho Vermelho",math.ceil(N/3))
    print("Vovozinha",math.ceil(N/3 - 1))
    print("Lobo Mau",math.ceil(N/3 - 1))
else: 
    print("Chapeuzinho Vermelho",math.ceil(N/3)) 
    print("Vovozinha",math.ceil(N/3))
    print("Lobo Mau",math.ceil(N/3))




