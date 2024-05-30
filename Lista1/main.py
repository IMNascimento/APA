from ex1 import gerar_grafo_e_matriz, imprimir_matriz, calcular_indices_dos_vertices, calcular_numero_de_triangulos
from ex2 import gerar_matriz_binaria
from ex3 import triangular_superior_vetor
from ex4 import gerar_vetor_compactado
from ex5 import vetor_compactado_para_matriz
from ex6 import mapear_ij_para_k, mapear_ij_para_k_iterativo, mapear_ij_para_k_recursivo
from ex7 import mapear_k_para_ij, mapear_k_para_ij_iterativo
from ex8 import unir_vetores, intersectar_vetores

def main():
    matriz_adjacencia = None
    vetor_triangular = None
    vetor_compactado = None

    while True:
        print("\nMenu de Opções:")
        print("1. Executar exercício 1")
        print("2. Executar exercício 2")
        print("3. Executar exercício 3")
        print("4. Executar exercício 4")
        print("5. Executar exercício 5")
        print("6. Executar exercício 6")
        print("7. Executar exercício 7")
        print("8. Executar exercício 8")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")
        n_vertices = 10
        min_aresta = 1
        max_aresta = 10
        if opcao == "1":
            
            matriz = gerar_grafo_e_matriz(n_vertices, min_aresta, max_aresta)
            print("Matriz de Adjacência:")
            imprimir_matriz(matriz)
            indices = calcular_indices_dos_vertices(matriz)
            print("Índices dos vértices:", indices)
            triangulos = calcular_numero_de_triangulos(matriz)
            print("Número de triângulos:", triangulos)
        
        elif opcao == "2":
            matriz_adjacencia = gerar_matriz_binaria(n_vertices, min_aresta, max_aresta)
            print("Matriz de Adjacência Binaria:")
            imprimir_matriz(matriz_adjacencia)
    

        elif opcao == "3" and matriz_adjacencia is not None:
            vetor_triangular = triangular_superior_vetor(matriz_adjacencia)
            print("Vetor triangular superior (ex3):", vetor_triangular)

        elif opcao == "4" and matriz_adjacencia is not None:
            vetor_compactado = gerar_vetor_compactado(matriz_adjacencia)
            print("Vetor compactado:", vetor_compactado)

        elif opcao == "5":
            if matriz_adjacencia is None:
                print("Execute a opção 1 primeiro para gerar a matriz de adjacência.")
            else:
                vetor_compactado = gerar_vetor_compactado(matriz_adjacencia)
                matriz_recuperada = vetor_compactado_para_matriz(vetor_compactado, len(matriz_adjacencia))
                print("Matriz recuperada a partir do vetor compactado:")
                imprimir_matriz(matriz_recuperada)

        elif opcao == "6":
            i, j = 2, 3
            n_vertices = 10
            k = mapear_ij_para_k(i, j, n_vertices)
            print("Mapeamento ij->k:", k)
            k_iter = mapear_ij_para_k_iterativo(i, j, n_vertices)
            print("Mapeamento ij->k (iterativo):", k_iter)
            k_rec = mapear_ij_para_k_recursivo(i, j, n_vertices)
            print("Mapeamento ij->k (recursivo):", k_rec)

        elif opcao == "7":
            k = 17
            n_vertices = 10
            ij = mapear_k_para_ij(k, n_vertices)
            print("Mapeamento k->ij:", ij)
            ij_iter = mapear_k_para_ij_iterativo(k, n_vertices)
            print("Mapeamento k->ij (iterativo):", ij_iter)

        elif opcao == "8":
            matriz1 = gerar_grafo_e_matriz(n_vertices, min_aresta, max_aresta)
            matriz2 = gerar_matriz_binaria(n_vertices, min_aresta, max_aresta)
            vetor1 = triangular_superior_vetor(matriz1)
            vetor2 = triangular_superior_vetor(matriz2)
            print("Vetor 1:", vetor1)
            print("Vetor 2:", vetor2)
            vetor_unido = unir_vetores(vetor1, vetor2)
            print("União dos vetores:", vetor_unido)
            vetor_intersecao = intersectar_vetores(vetor1, vetor2)
            print("Interseção dos vetores:", vetor_intersecao)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida ou matriz não gerada. Tente novamente.")

if __name__ == "__main__":
    main()