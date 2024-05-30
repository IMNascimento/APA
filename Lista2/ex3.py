def kahn_topological_sort(graph, n):
    in_degree = [0] * n
    for i in range(n):
        for j in graph[i]:
            in_degree[j] += 1

    queue = [i for i in range(n) if in_degree[i] == 0]
    top_order = []

    while queue:
        vertex = queue.pop(0)
        top_order.append(vertex)
        for neighbor in graph[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(top_order) == n:
        return top_order
    else:
        return "Cycle detected"

# Exemplo de uso:
graph = [
    [1],  # 0 -> 1
    [2],  # 1 -> 2
    []    # 2
]
n = 3
print(kahn_topological_sort(graph, n))

#Explicação: O algoritmo de Kahn para ordenação topológica é utilizado para ordenar hierarquicamente os vértices de um DAG. Ele também pode detectar ciclos, indicando se a lista de ordenação topológica não inclui todos os vértices.