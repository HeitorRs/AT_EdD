import random
import time

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
        if not trocou:
            break

def testar_bubble_sort(tamanho_lista):
    lista = [random.randint(1, 1000) for _ in range(tamanho_lista)]
    
    inicio = time.time()
    bubble_sort(lista)
    fim = time.time()

    tempo_execucao = fim - inicio
    print(f"Tempo de execução para lista de {tamanho_lista}: {tempo_execucao:.4f} segundos")

testar_bubble_sort(1000)
testar_bubble_sort(10000)
