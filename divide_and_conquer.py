# dividir para conquistar: O(n log n)

def soma(lista):
    total = 0
    for x in lista:
        total += x
    return total

print(soma([1, 2, 3, 4])) # Saída: 10

# com função recursiva

def soma(lista):
    if not lista: # caso base: se a lista estiver vazia, retorna 0
        return 0
    else:
        return lista[0] + soma(lista[1:]) # caso recursivo: soma o primeiro elemento com a soma do restante da lista
print(soma([1, 2, 3, 4])) # Saída: 10

# conta numero de itens em uma lista

def conta_itens(lista):
    if not lista:
        return 0 # caso base: se a lista estiver vazia, retorna 0
    else:
        return 1 + conta_itens(lista[1:]) # caso recursivo: conta o primeiro elemento e soma com a contagem do restante da lista
print(conta_itens([1, 2, 3, 4])) # Saída: 4
    
# valor mais alto em uma lista]

def valor_mais_alto(lista):
    if len(lista) == 1:
        return lista[0] # caso base: se a lista tiver apenas um elemento, retorna esse elemento
    else:
        max_restante = valor_mais_alto(lista[1:]) # caso recursivo: encontra o valor mais alto do restante da lista
        return max(lista[0], max_restante) # compara o primeiro elemento com o valor mais alto do restante da lista e retorna o maior
print(valor_mais_alto([1, 2, 3, 4])) # Saída: 4