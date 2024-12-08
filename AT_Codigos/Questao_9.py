import random
import time

class Hashtable:
    def __init__(self, tamanho=100000):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self._hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                item = (chave, valor)
                return
        self.tabela[indice].append((chave, valor))

    def buscar(self, chave):
        indice = self._hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                return item[1]
        return None
    
#Gerando uma lista de 100.000 usuários fictícios
usuarios = []
for i in range(100000):
    nome_usuario = f"user{i}"
    perfil = {"nome": f"User {i}", "idade": random.randint(18, 50), "cidade": "Cidade X"}
    usuarios.append((nome_usuario, perfil))

random.shuffle(usuarios)

print(usuarios)

hashtable = Hashtable()
for nome_usuario, perfil in usuarios:
    hashtable.inserir(nome_usuario, perfil)

#Teste de busca em uma hashtable
nome_busca = "user98767"
start_time = time.time()
perfil_hashtable = hashtable.buscar(nome_busca)
hashtable_time = time.time() - start_time

print(f"Perfil encontrado: {perfil_hashtable}")
print(f"Tempo de busca na hashtable: {hashtable_time:.6f} segundos")

#Teste de busca em uma lista (busca sequencial)
start_time = time.time()
perfil_lista = None
for nome_usuario, perfil in usuarios:
    if nome_usuario == nome_busca:
        perfil_lista = perfil
        break
lista_time = time.time() - start_time

print(f"Perfil encontrado na lista: {perfil_lista}")
print(f"Tempo de busca na lista: {lista_time:.6f} segundos")

