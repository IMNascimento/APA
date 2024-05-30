import random

def gerar_matriz_adjacencia_binaria(n_vertices, min_arestas, max_arestas):
    # Criar uma matriz de adjacência binária inicialmente preenchida com zeros
    matriz_adjacencia = [[0] * n_vertices for _ in range(n_vertices)]
    
    # Determinar o número total de arestas a serem adicionadas
    n_arestas = random.randint(min_arestas * n_vertices, max_arestas * n_vertices)
    
    # Adicionar arestas aleatoriamente até alcançar o número desejado
    adicionar_arestas = 0
    tentativas = 0
    max_tentativas = n_arestas * 10  # Define um limite para tentativas de adicionar arestas

    while adicionar_arestas < n_arestas and tentativas < max_tentativas:
        # Selecionar dois vértices aleatórios
        u = random.randint(0, n_vertices - 1)
        v = random.randint(0, n_vertices - 1)

        # Adicionar uma aresta se não houver uma já entre esses dois vértices
        if u != v and matriz_adjacencia[u][v] == 0:
            matriz_adjacencia[u][v] = 1
            matriz_adjacencia[v][u] = 1  # Garantir a simetria, já que o grafo é não orientado
            adicionar_arestas += 1
        tentativas += 1

    # Verifica se o loop foi terminado devido à falta de possibilidades de adição de novas arestas
    if tentativas >= max_tentativas:
        print("Atingido o limite máximo de tentativas para adicionar arestas. Arestas adicionadas:", adicionar_arestas)

    return matriz_adjacencia

# Configurações e execução do código
n_vertices = 10
min_arestas = 1
max_arestas = 10
matriz_adjacencia_binaria = gerar_matriz_adjacencia_binaria(n_vertices, min_arestas, max_arestas)

# Imprimir a matriz de adjacência gerada
for linha in matriz_adjacencia_binaria:
    print(linha)