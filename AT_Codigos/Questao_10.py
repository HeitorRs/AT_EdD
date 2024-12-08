class Navegador:
    def __init__(self, urls_iniciais):
        self.pilha_atual = []
        self.pilha_retorno = []
        self.urls_iniciais = urls_iniciais
        if urls_iniciais:
            self.pilha_atual.append(urls_iniciais[0])

    def voltar(self):
        if len(self.pilha_atual) > 1:
            pagina_atual = self.pilha_atual.pop()
            self.pilha_retorno.append(pagina_atual)
            print(f"Voltando para: {self.pilha_atual[-1]}")
        else:
            print("Não há mais páginas para voltar.")

    def avancar(self):
        if self.pilha_retorno:
            prox_pagina = self.pilha_retorno.pop()
            self.pilha_atual.append(prox_pagina)
            print(f"Avançando para: {prox_pagina}")
        else:
            print("Não há mais páginas para avançar.")

    def status(self):
        print("\nEstado atual:")
        print(f"Pilha Atual: {self.pilha_atual}")
        print(f"Pilha de Retorno: {self.pilha_retorno}\n")


#Simulação com interface
def executar_navegador():
    urls_iniciais = [
        "https://cardapio.com",
        "https://cardapio.com/menu",
        "https://cardapio.com/menu/almoço",
        "https://cardapio.com/menu/almoço/italiano"
    ]

    navegador = Navegador(urls_iniciais)

    for url in urls_iniciais[1:]:
        navegador.pilha_atual.append(url)

    print("Bem-vindo ao Simulador de Navegação")
    print("Você pode usar 'Voltar' ou 'Avançar' para navegar entre páginas.")
    print("Comandos disponíveis:")
    print("1. Voltar")
    print("2. Avançar")
    print("3. Mostrar estado")
    print("4. Sair")

    while True:
        try:
            print("\nEscolha uma ação:")
            opcao = int(input("Digite o número da ação: "))

            if opcao == 1:
                navegador.voltar()
            elif opcao == 2:
                navegador.avancar()
            elif opcao == 3:
                navegador.status()
            elif opcao == 4:
                print("Encerrando o simulador. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")


executar_navegador()

