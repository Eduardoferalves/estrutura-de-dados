import sys

def ordenar_pares_e_impares(numeros: list[int]) -> list[int]:
    """
    Separa e ordena os números inteiros conforme os critérios:
    1. Números pares em ordem crescente.
    2. Números ímpares em ordem decrescente.
    Complexidade: O(N log N) tempo e O(N) espaço auxiliar.
    """
    pares: list[int] = []
    impares: list[int] = []

    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    pares.sort()
    impares.sort(reverse=True)

    return pares + impares

def main():
    # Leitura otimizada para lidar eficientemente com até 10^5 entradas
    entrada = sys.stdin.read().split()
    if not entrada:
        return

    n = int(entrada[0])
    numeros = [int(x) for x in entrada[1 : n + 1]]

    resultado = ordenar_pares_e_impares(numeros)
    sys.stdout.write("\n".join(map(str, resultado)) + "\n")


if __name__ == "__main__":
    main()