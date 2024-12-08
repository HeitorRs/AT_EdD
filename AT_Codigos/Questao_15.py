class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = No(chave)
        else:
            self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, no, chave):
        if chave < no.chave:
            if no.esquerda is None:
                no.esquerda = No(chave)
            else:
                self._inserir_recursivo(no.esquerda, chave)
        else:
            if no.direita is None:
                no.direita = No(chave)
            else:
                self._inserir_recursivo(no.direita, chave)

    def buscar_minimo(self):
        return self._buscar_minimo(self.raiz)

    def _buscar_minimo(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no.chave

    def buscar_maximo(self):
        return self._buscar_maximo(self.raiz)

    def _buscar_maximo(self, no):
        while no.direita is not None:
            no = no.direita
        return no.chave

def testar_bst():
    notas = [85, 70, 95, 60, 75, 90, 100]
    
    bst = BST()
    
    for nota in notas:
        bst.inserir(nota)
    
    minimo = bst.buscar_minimo()
    maximo = bst.buscar_maximo()
    
    print(f"Nota mínima: {minimo}")
    print(f"Nota máxima: {maximo}")

testar_bst()
