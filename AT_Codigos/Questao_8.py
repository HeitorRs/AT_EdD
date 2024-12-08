def selection_sort(jogadores):
    n = len(jogadores)
    
    for i in range(n):
        indice_maximo = i
        for j in range(i + 1, n):
            if jogadores[j]['pontuacao'] > jogadores[indice_maximo]['pontuacao']:
                indice_maximo = j
        
        jogadores[i], jogadores[indice_maximo] = jogadores[indice_maximo], jogadores[i]

jogadores = [
    {"nome": "Heitor", "pontuacao": 1500},
    {"nome": "João", "pontuacao": 1250},
    {"nome": "Maria", "pontuacao": 2100},
    {"nome": "Letícia", "pontuacao": 1800}
]

selection_sort(jogadores)

for jogador in jogadores:
    print(f"{jogador['nome']}: {jogador['pontuacao']}")
