## Primeiro Trabalho Implementação – APA
1 – Gerar randomicamente um grafo não orientado com 100 vértices , com um número baixo 
de ligações ( de uma a dez vezes o número de vértices ). 
2 – Implementar um algoritmo que gere a representação matricial ( matriz adjacência binária )
3 – Implementar um algoritmo que, a partir da matriz, gere a representação vetorial ( vetor 
binário )de sua parte triangular superior. 
4 – Gerar o vetor compactado ( vetor de índices inteiros ) com endereçamento indireto. 
5 – Implementar um algoritmo que a partir do vetor compactado gere a matriz de adjacência.
6 – Implementar a função de mapeamento que a partir da entrada (i,j) da matriz de adjacência 
de ordem n acesse a posição k do vetor de índices. Implementar o cálculo analítico ( 
progressão aritmética ) e também os procedimentos iterativo e recursivo. 
7 – Implementar a função de mapeamento inversa que a partir do índice k do vetor acesse a 
posição (i,j) da matriz de adjacência de ordem n. Implementar o cálculo analítico ( algoritmo 
raiz quadrada ) e também o procedimento iterativo. 
8 – Implementar as operações de soma operação de união ) , produto direto ( operação de 
interseção ) entre duas matrizes utilizando suas respectivas representações vetoriais. 

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
