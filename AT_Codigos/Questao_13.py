def knapsack(valores, pesos, capacidade):
    n = len(valores)
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], valores[i - 1] + dp[i - 1][w - pesos[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacidade]

valores = [60, 100, 120]
pesos = [10, 20, 30]      
capacidade = 50           

resultado = knapsack(valores, pesos, capacidade)
print(f"Valor máximo que pode ser colocado na mochila: {resultado}")
