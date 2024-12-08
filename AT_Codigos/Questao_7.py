def verificar_duplicatas(lista):
    elementos_vistos = set()
    
    for item in lista:
        if item in elementos_vistos:
            return "Existem elementos duplicados"
        elementos_vistos.add(item)
    
    return "Não existem elementos duplicados"

lista = [1, 2, 3, 4, 5, 6, 7, 3]
print(verificar_duplicatas(lista))

lista_sem_duplicatas = [1, 2, 3, 4, 5, 6, 7]
print(verificar_duplicatas(lista_sem_duplicatas))
