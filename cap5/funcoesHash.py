# retorne 1 para qualquer chave, ou seja, independente da chave que for consultada, o valor retornado será sempre 1.
retorne_1 = dict() # cria um dicionário vazio
def retorna_1_chave(chave):
    retorne_1[chave] = 1 # atribui o valor 1 para a chave fornecida
    return retorne_1[chave] # retorna o valor associado à chave, que será sempre 1
print(retorna_1_chave("qualquer_chave")) # Saída: 1
print(retorna_1_chave("outra_chave")) # Saída: 1

# use o comprimento da string como indice para armazenar o valor, ou seja, o valor associado a cada chave será o comprimento da string da chave.
comprimento_chave = dict() # cria um dicionário vazio
def func_comprimento_chave(chave):
    comprimento_chave[chave] = len(chave) # atribui o comprimento da chave como valor associado à chave
    return comprimento_chave[chave] # retorna o valor associado à chave, que será o comprimento da string da chave
print(func_comprimento_chave("maçã")) # Saída: 5
print(func_comprimento_chave("banana")) # Saída: 6
print(func_comprimento_chave("abacate")) # Saída: 7

# primeiro caractere da string como indice para armazenar o valor, ou seja, o valor associado a cada chave será o primeiro caractere da string da chave.
primeiro_caractere = dict() # cria um dicionário vazio
def func_primeiro_caractere(chave):
    primeiro_caractere[chave] = chave[0] # atribui o primeiro caractere da chave como valor associado à chave
    return primeiro_caractere[chave] # retorna o valor associado à chave, que será o primeiro caractere da string da chave
print(func_primeiro_caractere("maçã")) # Saída: 'm'
print(func_primeiro_caractere("banana")) # Saída: 'b'
print(func_primeiro_caractere("abacate")) # Saída: 'a'
print(func_primeiro_caractere("abacaxi")) # Saída: 'a'

# mapeie cada letra por um número primo: a = 2, b = 3, c = 5, d = 7, e = 11, f = 13, g = 17, h = 19, i = 23, j = 29, k = 31, l = 37, m = 41, n = 43, o = 47, p = 53, q = 59, r = 61, s = 67, t = 71, u = 73, v = 79, w = 83, x = 89, y = 97, z = 101.
# Para uma string a função hash é a soma de todos os caracteres conforme o tamanho do hash, ou seja, se o tamanho é 10, o string "abc" 
# seria mapeado para (3 + 2 + 17) % 10 = 2.