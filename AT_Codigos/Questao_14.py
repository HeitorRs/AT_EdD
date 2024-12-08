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

    def buscar(self, chave):
        return self._buscar_recursivo(self.raiz, chave)

    def _buscar_recursivo(self, no, chave):
        if no is None or no.chave == chave:
            return no
        elif chave < no.chave:
            return self._buscar_recursivo(no.esquerda, chave)
        else:
            return self._buscar_recursivo(no.direita, chave)

def testar_bst():
    precos = [100, 50, 150, 30, 70, 130, 170]
    
    bst = BST()
    
    for preco in precos:
        bst.inserir(preco)
    
    resultado = bst.buscar(70)
    
    if resultado:
        print(f"Preço {resultado.chave} encontrado na árvore!")
    else:
        print("Preço não encontrado na árvore.")

testar_bst()
