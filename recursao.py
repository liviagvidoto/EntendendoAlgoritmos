#Enquanto o monte existir pegue a caixa e olhe o que tem dentro dela. Se achar a chave, ótimo! Se não achar, pegue as caixas dentro dela e repita o processo.

def procure_pela_chave(caixa_principal):
    pilha = main_box.crie_uma_pilha_para_busca()
    while pilha is not empty:
        caixa_atual = pilha.pegue_a_caixa()
        for item in caixa:
            if item.caixa():
                pilha.append(item)
            elif item.chave():
                print("Chave encontrada!")
                return True
    print("Chave não encontrada.")
    return False

# Recursão é uma técnica onde uma função chama a si mesma para resolver um problema. Ela é frequentemente usada para resolver problemas que podem ser divididos em subproblemas menores, como árvores, listas e algoritmos de ordenação.

def procure_pela_chave(caixa):
    for item in caixa:
        if item.caixa():
            procure_pela_chave(item)  # Chamada recursiva para procurar dentro da caixa
        elif item.chave():
            print("Chave encontrada!")
            return True
    return False

# "Os loops podem melhorar o desempenho do seu programa. A recursão melhora o desempenho do seu programador. Escolha o que for mais importante para sua situação" - Lewis Caldwall 

# executa sem parar

def regressiva(i):
    print(i)
    regressiva(i-1)

# Quando chamamos uma função recursiva devemos informar quando ela deve parar, toda função recursiva deve ter um caso base  e caso recursivo.

def regressiva(i):
    print(i)
    if i <= 1: # caso base if
        return
    else: # caso recursivo else
        regressiva(i-1)




