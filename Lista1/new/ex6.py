#Cálculo analítico

def mapear_ij_para_k(i, j, n):
    if i > j:
        i, j = j, i
    return (n * i) - (i * (i + 1) // 2) + (j - i - 1)

#Procedimento iterativo

def mapear_ij_para_k_iterativo(i, j, n):
    if i > j:
        i, j = j, i
    k = 0
    for row in range(i):
        k += n - row - 1
    k += j - i - 1
    return k


#Procedimento recursivo

def mapear_ij_para_k_recursivo(i, j, n):
    if i > j:
        i, j = j, i
    if i == 0:
        return j - 1
    return (n - i) + mapear_ij_para_k_recursivo(i - 1, j, n)