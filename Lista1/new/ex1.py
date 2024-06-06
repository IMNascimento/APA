import random

def gerar_grafo_e_matriz(n_vertices, min_aresta, max_aresta):
    max_arestas_possivel = n_vertices * (n_vertices - 1) // 2
    n_arestas = random.randint(min_aresta * n_vertices, min(max_aresta * n_vertices, max_arestas_possivel))
    matriz_adjacencia = [[0] * n_vertices for _ in range(n_vertices)]
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




#gerar_grafo_e_matriz: O(n2)
#imprimir_matriz O(n2)
#calcular_indices_dos_vertices O(n2)
#calcular_numero_de_triangulos O(n3)

#Portanto, as funções apresentadas possuem complexidades diferentes,
# com a função de cálculo de triângulos sendo a mais complexa, com uma complexidade cúbica
# O(n3). As outras funções têm complexidade quadrática O(n2).


