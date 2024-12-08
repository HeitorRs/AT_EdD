import random

def busca_binaria(lista, isbn_procurado):
    inicio, fim = 0, len(lista) - 1
    iteracoes = 0
    
    while inicio <= fim:
        iteracoes += 1
        meio = (inicio + fim) // 2
        if lista[meio] == isbn_procurado:
            return meio, iteracoes
        elif lista[meio] < isbn_procurado:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, iteracoes


def busca_linear(lista, isbn_procurado):
    iteracoes = 0
    for i, isbn in enumerate(lista):
        iteracoes += 1
        if isbn == isbn_procurado:
            return i, iteracoes
    return -1, iteracoes


isbn_lista = sorted(random.sample(range(1_000_000, 10_000_000), 100_000))
isbn_procurado = random.choice(isbn_lista)

indice_binaria, iteracoes_binaria = busca_binaria(isbn_lista, isbn_procurado)

indice_linear, iteracoes_linear = busca_linear(isbn_lista, isbn_procurado)

print(f"ISBN procurado: {isbn_procurado}")
print(f"Busca Binária: Índice = {indice_binaria}, Iterações = {iteracoes_binaria}")
print(f"Busca Linear: Índice = {indice_linear}, Iterações = {iteracoes_linear}")
