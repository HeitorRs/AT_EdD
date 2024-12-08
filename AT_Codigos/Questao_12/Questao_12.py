import os

def listar_arquivos(diretorio):
    try:
        for item in os.listdir(diretorio):
            caminho_completo = os.path.join(diretorio, item)

            if os.path.isfile(caminho_completo):
                print(f"\"{item}\" | Caminho: \"{caminho_completo}\"")

            elif os.path.isdir(caminho_completo):
                listar_arquivos(caminho_completo)
    except FileNotFoundError:
        print(f"O diretório não foi encontrado: {diretorio}")

diretorio_inicial = "Questao_12/Arquivos"
listar_arquivos(diretorio_inicial)