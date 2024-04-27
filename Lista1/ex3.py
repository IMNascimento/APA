def matriz_para_vetor_binario(matriz):
    n = len(matriz)  # assume-se que a matriz é quadrada
    vetor_binario = []
    
    for i in range(n):
        for j in range(i, n):
            if matriz[i][j] != 0:
                vetor_binario.append(1)
            else:
                vetor_binario.append(0)

    return vetor_binario

# Exemplo de matriz para testar o algoritmo
matriz_exemplo = [
    [1, 2, 0],
    [0, 3, 0],
    [0, 0, 4]
]

# Gerar o vetor binário
vetor_binario_resultante = matriz_para_vetor_binario(matriz_exemplo)

print(vetor_binario_resultante)