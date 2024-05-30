import random

def gera_grafo_q1(nmr_arestas, nmr_vertices):
    arestas = [[0, 0] for _ in range(nmr_arestas)]
    i = 0
    while i < nmr_arestas:
        arestas[i][0] = random.randint(1, nmr_vertices)
        arestas[i][1] = random.randint(1, nmr_vertices)
        if arestas[i][0] != arestas[i][1]:
            i += 1

    print("\nGrafo aleatório: \n")
    for i in range(nmr_vertices):
        print(f"\t{i+1}-> [ ", end="")
        contador = 0
        for j in range(nmr_arestas):
            if arestas[j][0] == i+1:
                print(arestas[j][1], end=" ")
                contador += 1
            elif arestas[j][1] == i+1:
                print(arestas[j][0], end=" ")
                contador += 1
            elif j == nmr_arestas - 1 and contador == 0:
                print("Vertice sem arestas", end="")
        print(" ]")
    return arestas

def questao1():
    random.seed()
    v = 10  # Número de vértices
    a = v + (v * random.randint(0, 8))  # Geração de 100 a 1000 vértices
    return gera_grafo_q1(a, v)

def questao2(arestas):
    print("\nMatriz de adjacências: \n")
    matriz = [[0]*10 for _ in range(10)]
    for i in range(len(arestas)):
        matriz[arestas[i][0] - 1][arestas[i][1] - 1] = 1
        matriz[arestas[i][1] - 1][arestas[i][0] - 1] = 1

    for row in matriz:
        print(" ".join(map(str, row)))
    return matriz

def questao3(matriz):
    vetor = []
    contador = 0
    for i in range(100):
        for j in range(100):
            if i < j:
                vetor.append(matriz[i][j])
                contador += 1

    print("\n\nVetor Binário: \n\n")
    print(" ".join(map(str, vetor)))
    return vetor

def questao4(vetor_binario):
    vetor_compactado = []
    for i in range(len(vetor_binario)):
        if vetor_binario[i] == 1:
            vetor_compactado.append(i + 1)

    print("\n\nVetor Compactado: \n\n")
    print(" ".join(map(str, vetor_compactado)))
    return vetor_compactado

def questao5(vetor_compactado):
    matriz = [[0]*100 for _ in range(100)]
    contador_val_vetor_compactado = 0
    contador_pos_vetor_compactado = 0
    for i in range(100):
        for j in range(100):
            if i < j:
                contador_val_vetor_compactado += 1
                if contador_pos_vetor_compactado < len(vetor_compactado) and vetor_compactado[contador_pos_vetor_compactado] == contador_val_vetor_compactado:
                    matriz[i][j] = 1
                    matriz[j][i] = 1
                    contador_pos_vetor_compactado += 1
            if contador_pos_vetor_compactado >= len(vetor_compactado):
                break
        if contador_pos_vetor_compactado >= len(vetor_compactado):
            break

    print("\n\nNova Matriz: \n")
    for row in matriz:
        print(" ".join(map(str, row)))

def main():
    while True:
        questao = input("Selecione a questao de 1 a 8 ou 'q' para sair: ")
        if questao == 'q':
            break
        elif questao == '1':
            arestas = questao1()
        elif questao == '2':
            matriz = questao2(arestas)
        elif questao == '3':
            vetor_binario = questao3(matriz)
        elif questao == '4':
            vetor_compactado = questao4(vetor_binario)
        elif questao == '5':
            questao5(vetor_compactado)
        else:
            print("Questão inválida")

if __name__ == "__main__":
    main()