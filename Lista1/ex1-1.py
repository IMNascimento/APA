import random

def gerar_grafo_e_matriz(n_vertices, min_aresta, max_aresta):
    n_arestas = random.randint(min_aresta * n_vertices, max_aresta * n_vertices)
    matriz_adjacencia = [[0] * n_vertices for _ in range(n_vertices)]
    
    # Adicionar ligações de forma aleatória até atingir o número desejado de ligações
    arestas_adicionadas = 0
    while arestas_adicionadas < n_arestas:
        u = random.randint(0, n_vertices - 1)
        v = random.randint(0, n_vertices - 1)
        if u != v and matriz_adjacencia[u][v] == 0:
            matriz_adjacencia[u][v] = 1
            matriz_adjacencia[v][u] = 1
            arestas_adicionadas += 1

    return matriz_adjacencia

def imprimir_matriz(matriz):
    for row in matriz:
        print(row)

def calcular_indices_dos_vertices(matriz):
    indices = [sum(row) for row in matriz]
    return indices

def calcular_numero_de_triangulos(matriz):
    n = len(matriz)
    triangulos = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matriz[i][j] and matriz[j][k] and matriz[k][i]:
                    triangulos += 1
    return triangulos // 6

# Configurações do grafo
n_vertices = 10
min_aresta = 1
max_aresta = 10

# Geração do grafo e cálculo de propriedades
matriz_adjacencia = gerar_grafo_e_matriz(n_vertices, min_aresta, max_aresta)
print("Matriz de Adjacência:")
imprimir_matriz(matriz_adjacencia)

indices = calcular_indices_dos_vertices(matriz_adjacencia)
print("Indices dos vértices:", indices)

triangulos = calcular_numero_de_triangulos(matriz_adjacencia)
print("Número de triângulos:", triangulos)