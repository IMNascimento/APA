#Cálculo analítico (algoritmo raiz quadrada)

import math

def mapear_k_para_ij(k, n):
    i = int(math.floor((2 * n - 1 - math.sqrt((2 * n - 1)**2 - 8 * k)) / 2))
    j = k + i + 1 - n * i + (i * (i + 1)) // 2
    return (i, j)

#Procedimento iterativo

def mapear_k_para_ij_iterativo(k, n):
    i = 0
    while k >= (n - i - 1):
        k -= (n - i - 1)
        i += 1
    j = k + i + 1
    return (i, j)