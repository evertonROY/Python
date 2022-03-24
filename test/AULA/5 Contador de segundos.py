C = int(input())
H = int(C/3600)
R = (C%3600)
S = int(R%60)
M = int(R/60)
print("%ih %im %is" %(H, M, S))
#print(H,'h'," ", M,'m'," ", S,'s', sep="")


