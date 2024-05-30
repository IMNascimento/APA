def gerar_vetor_triangular_superior(matriz_adjacencia):
    n_vertices = len(matriz_adjacencia)
    vetor_triangular_superior = []
    for i in range(n_vertices):
        for j in range(i + 1, n_vertices):
            vetor_triangular_superior.append(matriz_adjacencia[i][j])
    return vetor_triangular_superior


