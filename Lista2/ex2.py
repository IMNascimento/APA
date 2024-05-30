def dfs(graph, start, path, visited, all_paths):
    visited[start] = True
    path.append(start)
    if all(not visited[neigh] for neigh in graph[start]):
        all_paths.append(path.copy())
    else:
        for neighbor in graph[start]:
            if not visited[neighbor]:
                dfs(graph, neighbor, path, visited, all_paths)
    path.pop()
    visited[start] = False

def find_all_paths(graph, start_vertex):
    visited = [False] * len(graph)
    all_paths = []
    dfs(graph, start_vertex, [], visited, all_paths)
    return all_paths

# Exemplo de uso:
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}
start_vertex = 0
all_paths = find_all_paths(graph, start_vertex)
print(all_paths)

#Explicação: Este código realiza uma busca em profundidade (DFS) modificada para coletar todos os caminhos maximais e elementares de um vértice raiz em um grafo orientado.