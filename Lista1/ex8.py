#Soma (união)

def unir_vetores(vetor1, vetor2):
    return [max(a, b) for a, b in zip(vetor1, vetor2)]

#Produto direto (interseção)

def intersectar_vetores(vetor1, vetor2):
    return [a * b for a, b in zip(vetor1, vetor2)]