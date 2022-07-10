qnt_candidatos = int(input()) 

tempos_candidatos = list(map(int, input().split())) 

print(*sorted(tempos_candidatos)[0:8]) 