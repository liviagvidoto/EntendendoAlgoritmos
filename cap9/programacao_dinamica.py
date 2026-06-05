# Programação Dinâmica
# O nome "programação dinâmica" foi cunhado por Richard Bellman na década de 1950. Ele escolheu o termo "dinâmica" para transmitir a ideia de que o processo de resolução de problemas é fluida e adaptativa, e "programação" para se referir à formulação matemática dos problemas. A programação dinâmica é uma técnica poderosa para resolver problemas de otimização e contagem, onde a solução pode ser construída a partir de soluções menores.
 
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

print(fibonacci(10))  # Saída: 55