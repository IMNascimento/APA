import ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8
import random

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Gerar grafo não orientado")
        print("2. Gerar matriz de adjacência binária")
        print("3. Gerar vetor triangular superior")
        print("4. Gerar vetor compactado")
        print("5. Reconstruir matriz de adjacência a partir do vetor compactado")
        print("6. Mapeamento (i, j) para k")
        print("7. Mapeamento inverso k para (i, j)")
        print("8. União de vetores")
        print("9. Interseção de vetores")
        print("0. Sair")

        escolha = int(random.randint(0, 9))

        if escolha == 0:
            break
        elif escolha == 1:
            n_vertices = 100
            min_arestas = 1
            max_arestas = 10
            matriz_adjacencia = gerar_grafo_e_matriz(n_vertices, min_arestas, max_arestas)
            print("\nMatriz de Adjacência:")
            for linha in matriz_adjacencia:
                print(linha)
        elif escolha == 2:
            if 'matriz_adjacencia' not in locals():
                print("Gere o grafo primeiro.")
            else:
                print("\nMatriz de Adjacência:")
                for linha in matriz_adjacencia:
                    print(linha)
        elif escolha == 3:
            if 'matriz_adjacencia' not in locals():
                print("Gere o grafo primeiro.")
            else:
                vetor_triangular_superior = gerar_vetor_triangular_superior(matriz_adjacencia)
                print("\nVetor Triangular Superior:")
                print(vetor_triangular_superior)
        elif escolha == 4:
            if 'matriz_adjacencia' not in locals():
                print("Gere o grafo primeiro.")
            else:
                vetor_compactado = gerar_vetor_compactado(matriz_adjacencia)
                print("\nVetor Compactado (Lista de Arestas):")
                print(vetor_compactado)
        elif escolha == 5:
            if 'vetor_compactado' not in locals():
                print("Gere o vetor compactado primeiro.")
            else:
                matriz_reconstruida = vetor_compactado_para_matriz(vetor_compactado, n_vertices)
                print("\nMatriz de Adjacência Reconstruída:")
                for linha in matriz_reconstruida:
                    print(linha)
        elif escolha == 6:
            i = int(input("Digite i: "))
            j = int(input("Digite j: "))
            k = mapear_ij_para_k(i, j, n_vertices)
            print(f"\nMapeamento de ({i}, {j}) para k: {k}")
        elif escolha == 7:
            k = int(input("Digite k: "))
            i, j = mapear_k_para_ij(k, n_vertices)
            print(f"\nMapeamento inverso de k={k} para (i, j): ({i}, {j})")
        elif escolha == 8:
            if 'vetor_triangular_superior' not in locals():
                print("Gere o vetor triangular superior primeiro.")
            else:
                vetor_unido = unir_vetores(vetor_triangular_superior, vetor_triangular_superior)
                print("\nVetor Unido (União):")
                print(vetor_unido)
        elif escolha == 9:
            if 'vetor_triangular_superior' not in locals():
                print("Gere o vetor triangular superior primeiro.")
            else:
                vetor_intersecao = intersectar_vetores(vetor_triangular_superior, vetor_triangular_superior)
                print("\nVetor Interseção (Produto Direto):")
                print(vetor_intersecao)

if __name__ == "__main__":
    main()