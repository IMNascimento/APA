def dfs_path(graph, start, end, path=None):
    if path is None:
        path = []

    path.append(start)
    if start == end:
        return path

    for neighbor in graph[start]:
        if neighbor not in path:
            result_path = dfs_path(graph, neighbor, end, path.copy())
            if result_path:
                return result_path

    return None

# Exemplo de uso:
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}
start_vertex = 0
end_vertex = 3
path = dfs_path(graph, start_vertex, end_vertex)
print("Path from", start_vertex, "to", end_vertex, ":", path)



#Explicação: Este algoritmo realiza uma busca em profundidade a partir de um vértice inicial.
# Ele segue caminhos até encontrar o vértice alvo, evitando ciclos ao verificar se o vértice já está no caminho atual. 
#Se o vértice alvo é encontrado, o caminho até ele é retornado.