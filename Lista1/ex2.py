import numpy as np
import random

def gerar_matriz_adjacencia_binaria(n_vertices, min_arestas, max_arestas):
    # Criar uma matriz de adjacência binária inicialmente preenchida com zeros
    matriz_adjacencia = np.zeros((n_vertices, n_vertices), dtype=int)
    
    # Determinar o número total de arestas a serem adicionadas
    n_arestas = random.randint(min_arestas * n_vertices, max_arestas * n_vertices)

    # Adicionar arestas aleatoriamente até alcançar o número desejado
    adicionar_arestas = 0
    while adicionar_arestas < n_arestas:
        # Selecionar dois vértices aleatórios
        u, v = random.sample(range(n_vertices), 2)
        # Adicionar uma aresta se não houver uma já entre esses dois vértices
        if matriz_adjacencia[u, v] == 0 and u != v:
            matriz_adjacencia[u, v] = 1
            matriz_adjacencia[v, u] = 1  # Garantir a simetria, já que o grafo é não orientado
            adicionar_arestas += 1

    return matriz_adjacencia

# Definições para o exemplo
n_vertices = 10
min_arestas = 1  # mínimo de arestas (1x número de vértices)
max_arestas = 10  # máximo de arestas (10x número de vértices)

# Gerar a matriz de adjacência binária
matriz_adjacencia_binaria = gerar_matriz_adjacencia_binaria(n_vertices, min_arestas, max_arestas)

# Imprimir a matriz de adjacência gerada
print(matriz_adjacencia_binaria)