# tabelas hash são estruturas de dados que armazenam pares de chave-valor, permitindo acesso rápido aos valores com base nas chaves. 
# Elas são amplamente utilizadas em programação para implementar dicionários, conjuntos e outras estruturas de dados eficientes.

# Exemplo de implementação de uma tabela hash simples em Python

caderno = dict() # cria um dicionário vazio, que é uma implementação de tabela hash em Python
caderno["maçã"] = 0.67
caderno["leite"] = 1.49
caderno["abacate"] = 1.49
print(caderno)

print(caderno["maçã"]) # Saída: 0.67
print(caderno["leite"]) # Saída: 1.49
print(caderno["abacate"]) # Saída: 1.49 

# lista telefonica

agenda = dict() # cria um dicionário vazio para armazenar a agenda telefônica
agenda["Jenny"] = "123-456-7890"
agenda["Emergency"] = "190"
agenda["Mom"] = "111-222-3333"
print(agenda)

# evitando entradas duplicadas
# votação

votaram = {} # cria um dicionário vazio para armazenar os votos

def verificar_voto(nome):
    if votaram.get(nome): # verifica se o nome já está presente no dicionário
        print("Você já votou!") # se o nome estiver presente, exibe uma mensagem de aviso
    else:
        votaram[nome] = True # se o nome não estiver presente, adiciona o nome ao dicionário para marcar que a pessoa votou
        print(f"Obrigado por votar, {nome}!") # exibe uma mensagem de agradecimento

# quando alguém chegar para votar, verifica se o nome da pessoa já está presente no dicionário de votos. 
# Se estiver, significa que a pessoa já está no hash, se não estiver, a pessoa é adicionada ao hash para marcar que ela votou. 
# Isso garante que cada pessoa só possa votar uma vez, evitando votos duplicados.

valor = votaram.get("Tom") # verifica se "Tom" já votou, retorna None se não tiver votado
print(valor) # Saída: None (Tom ainda não votou)

# testes

verificar_voto("Tom") # Saída: Obrigado por votar, Tom!
verificar_voto("Mike") # Saída: Obrigado por votar, Mike!
verificar_voto("Mike") # Saída: Você já votou!

# utilizando as tabelas hash como cache

cache = {} # cria um dicionário vazio para armazenar os resultados em cache
def pega_pagina(url):
    if cache.get(url): # verifica se a URL já está presente no cache
        return cache[url] # se estiver presente, retorna o resultado armazenado no cache
    else:
        dados = pega_dados_do_servidor(url)
        cache[url] = dados # se não estiver presente, obtém os dados do servidor e armazena no cache
        return dados # retorna os dados obtidos do servidor
    
def pega_dados_do_servidor(url): # Simulação de uma função que obtém dados do servidor
    return f"Dados da {url}" # Retorna uma string simulando os dados obtidos do servidor 