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

    def remover(self, chave):
        self.raiz = self._remover_recursivo(self.raiz, chave)

    def _remover_recursivo(self, no, chave):
        if no is None:
            return no
        
        if chave < no.chave:
            no.esquerda = self._remover_recursivo(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._remover_recursivo(no.direita, chave)
        else:
            if no.esquerda is None:
                temp = no.direita
                no = None
                return temp
            elif no.direita is None:
                temp = no.esquerda
                no = None
                return temp

            temp = self._menor_no(no.direita)
            no.chave = temp.chave
            no.direita = self._remover_recursivo(no.direita, temp.chave)
        
        return no

    def _menor_no(self, no):
        current = no
        while current.esquerda is not None:
            current = current.esquerda
        return current

    def exibir_em_ordem(self):
        valores = []
        self._em_ordem_recursivo(self.raiz, valores)
        print("Árvore em ordem crescente:", valores)

    def _em_ordem_recursivo(self, no, valores):
        if no:
            self._em_ordem_recursivo(no.esquerda, valores)
            valores.append(no.chave)
            self._em_ordem_recursivo(no.direita, valores)

def testar_bst():
    codigos = [45, 25, 65, 20, 30, 60, 70]
    
    bst = BST()
    
    for codigo in codigos:
        bst.inserir(codigo)
    
    print("Árvore antes das remoções:")
    bst.exibir_em_ordem()

    bst.remover(20)
    bst.exibir_em_ordem()

    bst.remover(25)
    bst.exibir_em_ordem()

    bst.remover(45)
    bst.exibir_em_ordem()

testar_bst()
