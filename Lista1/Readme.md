## Primeiro Trabalho Implementação – APA
1 – Gerar randomicamente um grafo não orientado com 100 vértices , com um número baixo 
de ligações ( de uma a dez vezes o número de vértices ). <br>

2 – Implementar um algoritmo que gere a representação matricial ( matriz adjacência binária )<br>

3 – Implementar um algoritmo que, a partir da matriz, gere a representação vetorial ( vetor 
binário )de sua parte triangular superior. <br>

4 – Gerar o vetor compactado ( vetor de índices inteiros ) com endereçamento indireto. <br>

5 – Implementar um algoritmo que a partir do vetor compactado gere a matriz de adjacência.<br>

6 – Implementar a função de mapeamento que a partir da entrada (i,j) da matriz de adjacência 
de ordem n acesse a posição k do vetor de índices. Implementar o cálculo analítico ( 
progressão aritmética ) e também os procedimentos iterativo e recursivo.<br> 

7 – Implementar a função de mapeamento inversa que a partir do índice k do vetor acesse a 
posição (i,j) da matriz de adjacência de ordem n. Implementar o cálculo analítico ( algoritmo 
raiz quadrada ) e também o procedimento iterativo. <br>

8 – Implementar as operações de soma operação de união ) , produto direto ( operação de 
interseção ) entre duas matrizes utilizando suas respectivas representações vetoriais. <br>

<b>Obs.: Todos os algoritmos devem ser testados bem como determinado as suas funções de 
complexidade.</b>


exemplo da possibilidade:
import random

def gerar_grafo(num_vertices, num_arestas):
    if num_arestas < num_vertices - 1:
        print("Número de arestas é muito baixo para conectar todos os vértices.")
        return

    # Inicializa os vértices
    vertices = list(range(num_vertices))

    # Inicializa um conjunto para armazenar as arestas de forma única
    arestas = set()

    # Garante que o grafo é conectado
    for i in range(1, num_vertices):
        arestas.add((min(i, i-1), max(i, i-1)))

    # Adiciona arestas aleatórias até alcançar o número desejado
    while len(arestas) < num_arestas:
        a = random.randint(0, num_vertices - 1)
        b = random.randint(0, num_vertices - 1)
        if a != b:
            arestas.add((min(a, b), max(a, b)))

    return list(arestas)

# Número de vértices
n_vertices = 100
# Número de arestas
n_arestas = random.randint(n_vertices, 10 * n_vertices)

# Gerar o grafo
grafo = gerar_grafo(n_vertices, n_arestas)
print("Número de arestas:", len(grafo))
print("Arestas:", grafo)



## possibilidade do ex 2 

import random

def criar_grafo(n_vertices, n_arestas):
    # Cria uma matriz de adjacência 100x100 inicializada com zeros
    matriz_adjacencia = [[0] * n_vertices for _ in range(n_vertices)]
    
    # Lista para controlar a conexão dos vértices
    connected = set()

    # Garantir que o grafo é pelo menos conectado (criando uma árvore)
    for i in range(1, n_vertices):
        a = random.randint(0, i-1)
        matriz_adjacencia[a][i] = 1
        matriz_adjacencia[i][a] = 1
        connected.add((a, i))
        connected.add((i, a))

    # Adicionar arestas aleatórias até atingir o número desejado
    while len(connected) // 2 < n_arestas:
        a = random.randint(0, n_vertices - 1)
        b = random.randint(0, n_vertices - 1)
        if a != b and (a, b) not in connected and (b, a) not in connected:
            matriz_adjacencia[a][b] = 1
            matriz_adjacencia[b][a] = 1
            connected.add((a, b))
            connected.add((b, a))

    return matriz_adjacencia

# Número de vértices e arestas
n_vertices = 100
n_arestas = random.randint(n_vertices, 10 * n_vertices)

# Gerar a matriz de adjacência
matriz_adj = criar_grafo(n_vertices, n_arestas)

# Imprimir parte da matriz para verificação
for linha in matriz_adj[:5]:  # Mostra apenas as primeiras 5 linhas para brevidade
    print(linha[:5])
