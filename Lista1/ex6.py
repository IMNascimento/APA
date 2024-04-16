def calcular_k_analitico(i, j, n):
    return (i * (2 * n - i + 1)) // 2 + (j - i)

def calcular_k_iterativo(i, j, n):
    k = 0
    for linha in range(n):
        for coluna in range(linha, n):
            if linha == i and coluna == j:
                return k
            k += 1
    return -1  # Não encontrou (i, j) dentro dos limites da matriz triangular superior

def calcular_k_recursivo(i, j, n, linha=0, coluna=0, k=0):
    if linha > n or coluna > n:
        return -1  # Fora dos limites
    if linha == i and coluna == j:
        return k
    # Incrementa coluna, e se atingir o fim da linha, reseta para a próxima linha
    proxima_linha, proxima_coluna = (linha, coluna + 1) if coluna < n - 1 and coluna >= linha else (linha + 1, linha + 1)
    return calcular_k_recursivo(i, j, n, proxima_linha, proxima_coluna, k + 1 if coluna >= linha else k)

# Testando as funções para i=1, j=1, n=3 (deveria retornar índice 3 se i <= j)
i, j, n = 1, 1, 3
k_analitico = calcular_k_analitico(i, j, n)
k_iterativo = calcular_k_iterativo(i, j, n)
k_recursivo = calcular_k_recursivo(i, j, n)
print(k_analitico, k_iterativo, k_recursivo)