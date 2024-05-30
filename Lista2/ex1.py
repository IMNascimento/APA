import numpy as np

def floyd_warshall(n, edges):
    # Inicializando a matriz de distâncias com valores infinitos
    dist = np.full((n, n), np.inf)
    for i in range(n):
        dist[i, i] = 0
    
    # Preenchendo a matriz com as distâncias diretas entre os vértices
    for u, v, w in edges:
        dist[u][v] = w

    # Atualizando a matriz com as menores distâncias usando o algoritmo de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def compute_average_distance(n, edges):
    dist = floyd_warshall(n, edges)
    average_distances = {i: np.mean([dist[i][j] for j in range(n) if i != j]) for i in range(n)}
    return average_distances

# Exemplo de uso:
n = 4  # Número de vértices
edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1)]  # Arestas com pesos
average_distances = compute_average_distance(n, edges)
print(average_distances)


#Explicação: Este algoritmo utiliza Floyd-Warshall para calcular a distância mais curta entre todos os pares de vértices em um grafo fortemente conexo e,
# em seguida, calcula a média das distâncias de cada vértice para todos os outros.