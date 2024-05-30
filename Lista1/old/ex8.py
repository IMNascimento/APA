def uniao_vetores(vetor1, vetor2):
    # Assume que vetor1 e vetor2 têm o mesmo comprimento
    return [v1 | v2 for v1, v2 in zip(vetor1, vetor2)]

def intersecao_vetores(vetor1, vetor2):
    # Assume que vetor1 e vetor2 têm o mesmo comprimento
    return [v1 & v2 for v1, v2 in zip(vetor1, vetor2)]

# Exemplo de uso com dois vetores
vetor_A = [1, 0, 1, 1, 0, 1]  # Representação da matriz A
vetor_B = [1, 1, 0, 1, 0, 0]  # Representação da matriz B

# Realiza a união e a interseção
uniao_resultante = uniao_vetores(vetor_A, vetor_B)
intersecao_resultante = intersecao_vetores(vetor_A, vetor_B)

print(uniao_resultante, intersecao_resultante)