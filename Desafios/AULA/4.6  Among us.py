qnt_players = int(input()) 
murder_score_list = list(map(int, input().split())) 
print(*sorted(murder_score_list)) 