def gerar_vetor_compactado(matriz_adjacencia):
    n_vertices = len(matriz_adjacencia)
    vetor_compactado = []
    for i in range(n_vertices):
        for j in range(i + 1, n_vertices):
            if matriz_adjacencia[i][j] == 1:
                vetor_compactado.append((i, j))
    return vetor_compactado