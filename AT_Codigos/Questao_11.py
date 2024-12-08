class FilaAtendimento:
    def __init__(self):
        self.fila = []

    def adicionar_cliente(self, nome):
        self.fila.append(nome)
        print(f"Cliente {nome} adicionado(a) à fila.")
        self.tamanho_fila()

    def atender_cliente(self):
        if self.fila:
            cliente = self.fila[0]
            del self.fila[0]
            print(f"Atendendo cliente: {cliente}")
        self.tamanho_fila()

    def tamanho_fila(self):
        if len(self.fila) == 0:
            print("Não há mais clientes na fila.")
        else:
            print(f"Tamanho da fila: {len(self.fila)}")


fila_atendimento = FilaAtendimento()
fila_atendimento.adicionar_cliente("Heitor")
fila_atendimento.atender_cliente()
fila_atendimento.adicionar_cliente("João")
fila_atendimento.adicionar_cliente("Letícia")
fila_atendimento.atender_cliente()
fila_atendimento.adicionar_cliente("Ana")
fila_atendimento.atender_cliente()
fila_atendimento.atender_cliente()