def ordenar_por_tamanho_estavel(palavras: list[str]) -> list[str]:
    """
    Ordena as palavras por tamanho em ordem decrescente de forma estável.
    Utiliza agrupamento em baldes (Bucket Sort) indexados pelo comprimento:
    - O agrupamento preserva a ordem relativa original dos empates (estabilidade).
    - Complexidade de tempo linear O(N), pois o tamanho das palavras é restrito.
    """
    baldes: dict[int, list[str]] = {}

    for palavra in palavras:
        tamanho = len(palavra)
        if tamanho not in baldes:
            baldes[tamanho] = []
        baldes[tamanho].append(palavra)

    resultado = []
    # Itera pelos comprimentos presentes em ordem decrescente
    for tamanho in sorted(baldes.keys(), reverse=True):
        resultado.extend(baldes[tamanho])

    return resultado

def main():
    n = int(input().strip())

    for _ in range(n):
        palavras = input().split()
        ordenadas = ordenar_por_tamanho_estavel(palavras)
        print(" ".join(ordenadas))

if __name__ == "__main__":
    main()