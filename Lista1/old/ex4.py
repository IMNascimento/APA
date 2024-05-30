def matriz_para_vetor_indices(matriz):
    n = len(matriz)  # assume-se que a matriz é quadrada
    vetor_indices = []
    indice_linear = 0  # Para acompanhar o índice no vetor linearizado
    
    for i in range(n):
        for j in range(i, n):
            if matriz[i][j] != 0:
                vetor_indices.append(indice_linear)
            indice_linear += 1
    
    return vetor_indices


# Exemplo de matriz para testar o algoritmo
matriz_exemplo = [
    [1, 2, 0],
    [0, 3, 0],
    [0, 0, 4]
]

# Gerar o vetor de índices para a mesma matriz de exemplo
vetor_indices_resultante = matriz_para_vetor_indices(matriz_exemplo)
print(vetor_indices_resultante)