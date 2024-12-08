def buscar_contato_por_nome(lista_contatos, nome_procurado):
    for contato in lista_contatos:
        if contato["nome"].lower() == nome_procurado.lower():
            return f"Número de telefone do(a) {nome_procurado}: {contato['telefone']}"
    return f"Contato do(a) '{nome_procurado}' não encontrado."


contatos = [
    {"nome": "Heitor", "telefone": "2191234-5678"},
    {"nome": "João", "telefone": "2192345-6789"},
    {"nome": "Maria", "telefone": "2193456-7890"}
]

nome_a_procurar = "Heitor"
resultado = buscar_contato_por_nome(contatos, nome_a_procurar)
print(resultado)
