# indices invertidos são bastante utilizados em ferramentas de busca

# exemplo de criação de um índice invertido a partir de uma lista de documentos

def criar_indice_invertido(documentos):
    indice_invertido = {} 
    for doc_id, text in enumerate(documentos):
        palavras = text.split() # dividindo o texto em palavras
        for palavra in palavras: # para cada palavra, um id é adicionado ao conjunto de ids associados a essa palavra
            if palavra not in indice_invertido: # se a palavra ainda não estiver no índice, um novo conjunto é criado para armazenar os ids dos documentos que contêm essa palavra
                indice_invertido[palavra] = set() # usando um conjunto para evitar duplicatas
            indice_invertido[palavra].add(doc_id) # adicionando o id do documento ao conjunto associado à palavra
    return indice_invertido # o índice invertido é um dicionário onde as chaves são palavras e os valores são conjuntos de ids de documentos que contêm essas palavras
