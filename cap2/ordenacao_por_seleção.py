# O(n)
# Ordenação por seleção percorre cada item do input, TEMPO cresce LINEARMENTE com o tamanho do input.

def buscaLinear(array, item):
    for i, item in enumerate(array):
        if item == item:
            return i
    return -1

def soma(array):
    total = 0
    for num in array:
        total += num
    return total