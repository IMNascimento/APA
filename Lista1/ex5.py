def vetor_compactado_para_matriz(vetor_compactado, n_vertices):
    matriz_adjacencia = [[0] * n_vertices for _ in range(n_vertices)]
    for (i, j) in vetor_compactado:
        matriz_adjacencia[i][j] = 1
        matriz_adjacencia[j][i] = 1
    return matriz_adjacencia