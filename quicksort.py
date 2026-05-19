# O Quick Sort é um algoritmo de ordenação eficiente que utiliza a técnica de "dividir para conquistar". Ele escolhe um elemento como pivô e particiona o array em duas partes:
# os elementos menores que o pivô e os elementos maiores que o pivô.
# Em seguida, ele recursivamente ordena as duas partes. O processo de partição é repetido até que o array esteja completamente ordenado.

def quick_sort(array):
    if len(array) < 2: # caso base: arrays com 0 ou 1 elemento já estão ordenados
        return array
    else:
        pivot = array[0] # escolhe o primeiro elemento como pivô
        menores = [i for i in array[1:] if i <= pivot] # sub-array dos elementos menores ou iguais ao pivô
        maiores = [i for i in array[1:] if i > pivot] # sub-array dos elementos maiores que o pivô
        return quick_sort(menores) + [pivot] + quick_sort(maiores) # ordena recursivamente os sub-arrays e combina os resultados
print(quick_sort([10, 5, 2, 3])) # Saída: [2, 3, 5, 10]