import networkx as nx
import random
import numpy as np

def gerar_grafo_e_matriz(n_vertices, min_aresta, max_aresta):
    # Gerar número aleatório de ligações dentro do intervalo especificado
    n_arestas = random.randint(min_aresta * n_vertices, max_aresta * n_vertices)
    
    # Criar um grafo não orientado
    G = nx.Graph()
    # Adicionar vértices ao grafo
    G.add_nodes_from(range(n_vertices))
    
    # Adicionar ligações de forma aleatória até atingir o número desejado de ligações
    while G.number_of_edges() < n_arestas:
        # Escolher dois vértices aleatoriamente de uma lista dos nós
        u, v = random.sample(list(G.nodes), 2)
        # Adicionar uma ligação entre os vértices se ainda não existir
        if not G.has_edge(u, v):
            G.add_edge(u, v)
    
    # Obter a matriz de adjacência do grafo
    matriz_adjacencia = nx.adjacency_matrix(G)
    return matriz_adjacencia

# Definir número de vértices
n_vertices = 10
# Gerar a matriz de adjacência do grafo com 10 vértices
matriz_exemplo = gerar_grafo_e_matriz(n_vertices, 1, 10)

# Converter a matriz de adjacência para formato denso e imprimir
matriz_densa = matriz_exemplo.todense()
print(matriz_densa)

# Calcular o indice de cada vértice usando a matriz de adjacência
indices = np.sum(matriz_densa, axis=1)
print("Indices dos vértices:", indices)

# Determinar o número de triângulos no grafo
triangulos = np.trace(matriz_densa @ matriz_densa @ matriz_densa) // 6
print("Número de triângulos:", triangulos)
  
