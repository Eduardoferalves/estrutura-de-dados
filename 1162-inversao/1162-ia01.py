def contar_trocas_bubble_sort(vagoes: list[int]) -> int:
    """
    Calcula o número de trocas entre vagões adjacentes usando o algoritmo Bubble Sort.
    Cada troca simula a operação da ponte giratória com dois vagões vizinhos.
    O total de trocas adjacentes corresponde exatamente ao número de inversões da lista.
    """
    n = len(vagoes)
    trocas = 0
    
    # Trabalhamos com uma cópia para preservar a lista original
    lista = vagoes.copy()

    for i in range(n):
        trocou = False
        for j in range(0, n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
                trocou = True
        # Se nenhuma troca ocorreu nesta passagem, os vagões já estão ordenados
        if not trocou:
            break

    return trocas

def main():
    casos = int(input().strip())

    for _ in range(casos):
        tamanho = int(input().strip())
        
        # Trata o caso de tamanho 0 se houver
        if tamanho == 0:
            print("Optimal train swapping takes 0 swaps.")
            continue

        vagoes = list(map(int, input().split()))
        total_trocas = contar_trocas_bubble_sort(vagoes)
        print(f"Optimal train swapping takes {total_trocas} swaps.")

if __name__ == "__main__":
    main()