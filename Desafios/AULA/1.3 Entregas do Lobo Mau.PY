#T = ('tamanho')   #60     100
#D = ('distancia') #20     51
#V = ('KM')        #1$     2$ 
#P = ('pedagio')   #10$    50$      
                  #90     250

'''Minha primeira solução'''
T, D = [int(x) for x in input().split()]
V, P = [int(x) for x in input().split()]
F = int(T*V+(int(T/D)*P))
print(F)

'''Minha segunda solução'''
T, D = input().split()
V, P = input().split()
T = int(T)
D = int(D)
V = int(V)
P = int(P)
F = int(T*V+(int(T/D)*P))
print(F)

'''
O Lobo Mau resolveu parar um pouco com as maldades, decidiu abrir uma
empresa de entregas e convidou Chapeuzinho Vermelho para ser sua sócia.
Certo dia, Chapeuzinho precisou levar doces e bolos para sua vovozinha.
Como todos sabem, ela mora longe, o caminho é deserto e o Coelho Mau mora ali
por perto. Sim, como o Lobo virou empresário, alguém tinha que tomar seu lugar
na floresta. Para passar pelo caminho da floresta, o Coelho passou a cobrar um
valor ‘V’ por km e um valor ‘P’ por pedágio. Assim, Chapeuzinho pediu uma
carona ao seu sócio e lá foi ela pela estrada a fora, já não tão sozinha, levar os
bolos e doces para a vovozinha.
Saiba que a estrada tem tamanho ‘T’, que os pedágios estão a uma distância
‘D’ um dos outros (igualmente espaçados) e que o primeiro pedágio está no
km ‘D’. Portanto, o começo da estrada não possui um pedágio, mas o seu final
pode estar logo após um pedágio (por exemplo, se a distância entre dois
pedágios consecutivos for de 20 km e a estrada tiver 60 km, Chapeuzinho
deve pagar um pedágio aos 20 km, aos 40 km e aos 60 km). Assim, calcule
quanto custará para a pobre Chapeuzinho passar pela floresta e levar os doces
para a vovozinha.
Entrada
A entrada é composta na primeira linha por 2 inteiros, ‘T’ e ‘D’ (1 <=
‘T’,‘D’ <= 1000), representando o tamanho da estrada e a distância entre os
pedágios. Na próxima linha serão fornecidos outros 2 inteiros, ‘V’ e ‘P’ (1 <=
‘V’,‘P’ <= 100), representando o valor por km de estrada e o valor por cada
pedágio.
Saída
Na saída será apresentado o valor total pela travessia da floresta.
Entrada        Saída
60 20
1 10            90
           
100 51
2 50            250

'''
