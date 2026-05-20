# algoritmo de Dijkstra é um algoritmo de busca de caminho mais curto em um grafo ponderado.
# Ele é usado para encontrar o caminho mais curto entre um nó inicial e um nó objetivo em um grafo com pesos nas arestas.

grafo = {}
grafo["inicio"] = {}

grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

print(grafo["inicio"].keys()) # Saída: dict_keys(['a', 'b'])

# grafo

grafo["a"] = {}
grafo["a"]["fim"] = 1
grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5
grafo["fim"] = {}
# vertice final não tem vizinhos

# custos

infinito = float("inf") # representa o infinito como um número muito grande
custos = {}
custos = {"a"} = 6
custos["b"] = 2
custos["fim"] = infinito

# pais

pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

processados = [] # lista para armazenar os nós já processados

# código completo do algoritmo de Dijkstra

nodo = custo_mais_baixo(custos) # encontra o nó com o custo mais baixo
while nodo is not None: # enquanto houver um nó para processar
    custo = custos[nodo] # obtém o custo do nó
    vizinhos = grafo[nodo] # obtém os vizinhos do nó
    for n in vizinhos.keys(): # para cada vizinho do nó
        novo_custo = custo + vizinhos[n] # calcula o novo custo para o vizinho
        if custos[n] > novo_custo:
            custos[n] = novo_custo # se o novo custo for menor, atualiza o custo do vizinho
            pais[n] = nodo # e atualiza o pai do vizinho para o nó atual
    processados.append(nodo) # adiciona o nó à lista de processados
    nodo = custo_mais_baixo(custos) # encontra o próximo nó

# função para encontrar o nó com o custo mais baixo
def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf") # inicializa o custo mais baixo como infinito
    nodo_custo_mais_baixo = None # inicializa o nó com o custo mais baixo como None
    for nodo in custos: # para cada nó nos custos
        custo = custos[nodo] # obtém o custo do nó
        if custo < custo_mais_baixo and nodo not in processados: # se o custo for menor que o custo mais baixo e o nó não tiver sido processado
            custo_mais_baixo = custo # atualiza o custo mais baixo
            nodo_custo_mais_baixo = nodo # e atualiza o nó com o custo mais baixo
    return nodo_custo_mais_baixo # retorna o nó com o custo mais baixo
