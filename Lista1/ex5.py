def reconstruir_matriz_de_adjacencia(vetor_indices, n):
    # Inicializa uma matriz nxn com zeros
    matriz_adjacencia = [[0] * n for _ in range(n)]
    
    # Calcula o número total de elementos na parte triangular superior, incluindo a diagonal
    num_elementos_triang_sup = n * (n + 1) // 2
    
    # Reconstrói a parte triangular superior
    for index in vetor_indices:
        # Determina i e j a partir do índice linear
        total = 0
        for i in range(n):
            for j in range(i, n):
                if total == index:
                    matriz_adjacencia[i][j] = 1
                    break
                total += 1
            if total > index:
                break
    
    # Copia os valores para a parte triangular inferior
    for i in range(n):
        for j in range(i + 1, n):
            matriz_adjacencia[j][i] = matriz_adjacencia[i][j]

    return matriz_adjacencia

# Chamando a função com o vetor de índices anterior e n = 3
matriz_adjacencia = reconstruir_matriz_de_adjacencia([0, 1, 3, 5], 3)
print(matriz_adjacencia)