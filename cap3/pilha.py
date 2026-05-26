# pilha de chamadas
def sauda(nome):
    print(f"Olá, {nome}!")
    sauda2(nome)
    print("preparando para dizer tchau...")
    tchau()

# A função sauda chama a função sauda2, que por sua vez chama a função tchau. A pilha de chamadas é a estrutura de dados que mantém o controle das funções que estão sendo executadas. #
# Quando uma função é chamada, ela é adicionada à pilha. Quando a função termina, ela é removida da pilha e o controle retorna para a função anterior.

def sauda2(nome):
   print(f"Como vai, {nome}?")

def tchau():
    print("Tchau!")

# pilha de chamada com recursão

def fatorial(x):
    if x == 1:
        return 1
    else:
        return x * fatorial(x-1)

x = 3
print(fatorial(x)) # Saída: 6