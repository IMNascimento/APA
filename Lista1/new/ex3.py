def triangular_superior_vetor(matriz):
    n = len(matriz)
    vetor_binario = []
    
    for i in range(n):
        for j in range(i + 1, n):
            vetor_binario.append(matriz[i][j])
    
    return vetor_binario

#A complexidade da função triangular_superior_vetor é O(n2)

