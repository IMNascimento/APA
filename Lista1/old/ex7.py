import math

def mapeamento_inverso_analitico(k, n):
   # Encontra a linha i usando o método analítico
    i = 0
    while (i * (2 * n - i + 1)) // 2 <= k:
        i += 1
    i -= 1  # Decrementa para obter o valor correto de i após ultrapassar o limite

    # Calcula o total de elementos até a linha i
    total_elementos_antes_i = (i * (2 * n - i + 1)) // 2

    # Calcula j baseado no valor de k
    j = k - total_elementos_antes_i + i
    
    return (i, j)

def mapeamento_inverso_iterativo(k, n):
    contador = 0
    for i in range(n):
        for j in range(i, n):
            if contador == k:
                return (i, j)
            contador += 1

# Testando as funções para k = 3 e n = 3
k, n = 3, 3
posicao_ij_analitico = mapeamento_inverso_analitico(k, n)
posicao_ij_iterativo = mapeamento_inverso_iterativo(k, n)
print(posicao_ij_analitico, posicao_ij_iterativo)