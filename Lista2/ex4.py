def dfs(graph, start, visited):
    stack = [start]
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            for neighbor in graph[vertex]:
                if not visited[neighbor]:
                    stack.append(neighbor)

def is_strongly_connected(graph, n):
    visited = [False] * n
    # Start DFS from the first vertex
    dfs(graph, 0, visited)
    # If any vertex is not visited, then return not strongly connected
    if not all(visited):
        return False

    # Create a transposed graph
    transposed_graph = [[] for _ in range(n)]
    for v in range(n):
        for w in graph[v]:
            transposed_graph[w].append(v)

    # Check connectivity in the transposed graph
    visited = [False] * n
    dfs(transposed_graph, 0, visited)
    if not all(visited):
        return False

    return True

# Exemplo de uso:
graph = [
    [1],      # 0 -> 1
    [2],      # 1 -> 2
    [0],      # 2 -> 0
    [2, 3]    # 3 -> 2, 3
]
n = 4
print(is_strongly_connected(graph, n))

#Explicação: Este código utiliza uma busca em profundidade para verificar se todos os vértices são alcançáveis a partir de qualquer vértice no grafo original
# e no grafo transposto. Se ambos os testes passarem, o grafo é fortemente conexo.