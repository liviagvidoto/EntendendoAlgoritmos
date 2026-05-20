# pesquisa em largura permite encontrar o caminho mais curto entre um nó inicial e um nó objetivo em um grafo não ponderado. 
# Ele explora todos os nós vizinhos antes de avançar para os próximos níveis do grafo.

grafo = {}
grafo["você"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []

# a ordem que adiciona os pares chave/valor não faz diferença

from collections import deque
fila_de_pesquisa = deque() # cria uma fila vazia
fila_de_pesquisa += grafo["você"] # adiciona os vizinhos do nó "você" à fila de pesquisa

while fila_de_pesquisa: # enquanto a fila de pesquisa não estiver vazia
    pessoa = fila_de_pesquisa.popleft() # remove o primeiro elemento da fila de pesquisa e o atribui à variável "pessoa"
    if pessoa == "thom": # verifica se a pessoa é "thom"
        print("Thom é um vendedor!") # se for, imprime que Thom é um vendedor
        break # e interrompe o loop
    else: # caso contrário
        fila_de_pesquisa += grafo[pessoa] # adiciona os vizinhos da pessoa à fila de pesquisa
return False # se a fila de pesquisa estiver vazia e Thom não tiver sido encontrado, retorna False

# código completo da função de pesquisa em largura
def pesquisa(nome):
    fila_de_pesquisa = deque() # cria uma fila vazia
    fila_de_pesquisa += grafo[nome]
    verficadas = [] # cria uma lista para armazenar os nós já verificados
    while fila_de_pesquisa: # enquanto a fila de pesquisa não estiver vazia
        pessoa = fila_de_pesquisa.popleft() # remove o primeiro elemento da fila de pesquisa e o atribui à variável "pessoa"
        if pessoa not in verficadas: # verifica se a pessoa ainda não foi verificada
            if pessoa == "thom": # verifica se a pessoa é "thom"
                print("Thom é um vendedor!") # se for, imprime  que Thom é um vendedor
                return True # e retorna True
            else: # caso contrário
                fila_de_pesquisa += grafo[pessoa] # adiciona os vizinhos da pessoa à fila de pesquisa
                verficadas.append(pessoa) # adiciona a pessoa à lista de verificados
    return False # se a fila de pesquisa estiver vazia e Thom não tiver sido encontrado, retorna False
print(pesquisa("você")) # Saída: Thom é um vendedor! True

