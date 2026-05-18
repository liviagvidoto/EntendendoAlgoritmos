# O(1) 
# tempo sempre CONSTANTE, independente do tamanho do input.

# exemplo1
def primeiroElemento(array):
    return array[0]

# exemplo2
def ultimoElemento(array):
    return array[-1]

# exemplo3
def par(n):
    return n % 2 == 0

# O(n)
# Percorre cada item do input, TEMPO cresce LINEARMENTE com o tamanho do input.

# exemplo4
def buscaLinear(array, item):
    for i, item in enumerate(array):
        if item == item:
            return i
    return -1

# exemplo5
def soma(array):
    total = 0
    for num in array:
        total += num
    return total

# O(log n)
# Busca binária é um exemplo clássico de algoritmo O(log n), onde o tempo de execução cresce LOGARITMICAMENTE com o tamanho do input.

# exemplo6
def pesquisaBinaria(lista, item):
    baixo = 0 #baixo e alto são os índices que delimitam a parte da lista onde o item pode estar
    alto = len(lista) - 1

    while baixo <= alto: #enquanto o intervalo for válido
        meio = (baixo + alto) // 2 #encontrar o índice do meio da lista
        chute = lista[meio]

        if chute == item: #acha o item, retorna o índice
            return meio
        if chute > item: #chute é maior que o item, então o item deve estar na metade inferior da lista
            alto = meio - 1
        else: #chute é menor que o item, então o item deve estar na metade superior da lista
            baixo = meio + 1

    return None #item não encontrado na lista

minhaLista = [1, 3, 5, 7, 9]
print(pesquisaBinaria(minhaLista, 3))  # Saída: 1
print(pesquisaBinaria(minhaLista, -1)) # Saída: None

# O(n log n)
# dividir o problema em subproblemas menores, resolver cada um e depois combinar as soluções. Exemplos: Merge Sort, Quick Sort.

# exemplo7
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    meio = len(arr) // 2
    esq = merge_sort(arr[:meio])   # divide
    dir = merge_sort(arr[meio:])   # divide

    return merge(esq, dir)         # combina

def merge(esq, dir):
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            resultado.append(esq[i]); i += 1
        else:
            resultado.append(dir[j]); j += 1
    return resultado + esq[i:] + dir[j:]

# O(n^2)
# Para cada item do input, o algoritmo percorre todo o input novamente. Exemplos: Bubble Sort, Selection Sort.

#exemplo8
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):           # loop externo: n vezes
        for j in range(n - i - 1):  # loop interno: ~n vezes
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def pares_duplicados(arr):
    pares = []
    for i in range(len(arr)):       # n
        for j in range(i + 1, len(arr)):  # n
            if arr[i] == arr[j]:
                pares.append((i, j))
    return pares

# O(2^n)
# O algoritmo gera todas as combinações possíveis de um conjunto de itens. Exemplos: Fibonacci recursivo, Subconjuntos.

#exemplo9
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
    # fib(5) → fib(4) + fib(3)
    #          fib(3)+fib(2)  fib(2)+fib(1)  ← árvore cresce exponencialmente

def todos_subconjuntos(arr):
    if not arr:
        return [[]]
    primeiro = arr[0]
    resto = todos_subconjuntos(arr[1:])   # resolve o resto
    com_primeiro = [[primeiro] + s for s in resto]
    return resto + com_primeiro

# O(n!)
# O algoritmo gera todas as permutações possíveis de um conjunto de itens. Exemplos: Permutações, Problema do Caixeiro Viajante.

def permutacoes(arr):
    if len(arr) <= 1:
        return [arr]

    resultado = []
    for i, elemento in enumerate(arr):
        resto = arr[:i] + arr[i+1:]          # remove o elemento atual
        for perm in permutacoes(resto):      # permuta o restante
            resultado.append([elemento] + perm)

    return resultado