def construct_game_graph(n):
    game_graph = {i: [] for i in range(n+1)}
    for i in range(n+1):
        for move in [1, 2, 3]:
            if i - move >= 0:
                game_graph[i].append(i - move)
    return game_graph

def winning_strategy(game_graph, n):
    # Inicializando o estado de vitória para cada configuração de moedas
    winning = [False] * (n + 1)
    for i in range(n + 1):
        if any(not winning[i - move] for move in [1, 2, 3] if i - move >= 0):
            winning[i] = True
    return winning

# Exemplo de uso:
n = 10
game_graph = construct_game_graph(n)
winning = winning_strategy(game_graph, n)
print("Estratégia vencedora:", winning)

# Determinar jogadas vencedoras:
def find_winning_moves(winning, position):
    return [move for move in [1, 2, 3] if position - move >= 0 and not winning[position - move]]

winning_moves = find_winning_moves(winning, n)
print("Jogadas vencedoras a partir de 10 moedas:", winning_moves)

#Explicação: Este código constrói o grafo do jogo onde cada estado é um número de moedas, e as arestas são as jogadas possíveis (remover 1, 2 ou 3 moedas). 
#A função winning_strategy determina se cada estado é uma posição de vitória, e find_winning_moves identifica as 
#jogadas que garantem uma vitória a partir de um dado número de moedas. A partir de 10 moedas, o jogador inicial tem uma estratégia vencedora se seguir as jogadas recomendadas.