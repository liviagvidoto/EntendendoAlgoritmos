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