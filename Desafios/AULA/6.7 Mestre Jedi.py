qnt_planetas_galaxia = int(input()) 

planetas_codigos = list(input().split()) 

qnt_planetas_para_visitar = int(input()) 

nomes_planetas_para_visitar = list(input().split()) 

matriz_de_distancia_planetas = [] 

for i in range(0, qnt_planetas_galaxia): 

    linha = list(map(int, input().split())) 

    matriz_de_distancia_planetas.append(linha) 

distancia_total = 0 

planeta_atual = planetas_codigos[0] 

primeiro_planeta_a_visitar = nomes_planetas_para_visitar[0] 

planetas_visitados = 0 

for planeta in nomes_planetas_para_visitar: 

    distancia_percorrida = matriz_de_distancia_planetas[planetas_codigos.index(planeta_atual)][planetas_codigos.index(planeta)] 

    planeta_atual = planetas_codigos[planetas_codigos.index(planeta)] 

    distancia_total += distancia_percorrida 

    planetas_visitados += 1 

print(distancia_total)