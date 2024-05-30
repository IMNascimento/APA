def calculate_slack(times, dependencies):
    early_start, early_finish, late_start, late_finish, slack = {}, {}, {}, {}, {}
    
    # Função para calcular os tempos mais cedo
    def dfs_early(node):
        if node in early_finish:
            return early_finish[node]
        est = max((dfs_early(dep) for dep in dependencies.get(node, [])), default=0)
        early_start[node] = est
        early_finish[node] = est + times[node]
        return early_finish[node]

    # Função para calcular os tempos mais tarde
    def dfs_late(node, project_finish_time):
        if node in late_start:
            return late_start[node]
        lft = min((dfs_late(child, project_finish_time) for child in dependencies.get(node, [])), default=project_finish_time)
        late_finish[node] = lft
        late_start[node] = lft - times[node]
        slack[node] = late_start[node] - early_start[node]
        return late_start[node]

    # Calcular tempos mais cedo
    for node in times:
        dfs_early(node)
    
    # Calcular tempos mais tarde
    project_finish_time = max(early_finish.values())
    for node in times:
        dfs_late(node, project_finish_time)

    return early_start, early_finish, late_start, late_finish, slack

# Exemplo de uso:
times = {0: 3, 1: 2, 2: 1, 3: 4}
dependencies = {1: [0], 2: [1], 3: [1]}
results = calculate_slack(times, dependencies)
print("Slack times:", results[4])

#Explicação: Este código define uma rede PERT com tempos de duração e dependências. Ele usa duas funções DFS para calcular os tempos de início e término mais
# cedo e mais tarde de cada atividade. A folga é calculada como a diferença entre os tempos de início mais tarde e mais cedo de cada atividade.
# O código calcula esses valores para todas as atividades e retorna os resultados.