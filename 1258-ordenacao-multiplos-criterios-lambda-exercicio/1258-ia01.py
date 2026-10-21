import sys

# Mapeamento explícito para a ordem decrescente de tamanho ('P' > 'M' > 'G')
PRIORIDADE_TAMANHO = {"P": 0, "M": 1, "G": 2}

def ordenar_camisetas(pedidos: list[tuple[str, str, str]]) -> list[tuple[str, str, str]]:
    """
    Ordena os pedidos de camisetas utilizando função lambda com múltiplos critérios:
    1. Cor em ordem alfabética ascendente ('branco' antes de 'vermelho').
    2. Tamanho em ordem descendente ('P' antes de 'M' e 'M' antes de 'G').
    3. Nome do aluno em ordem alfabética ascendente.
    """
    return sorted(
        pedidos,
        key=lambda item: (
            item[1],                         # 1º critério: Cor ascendente
            PRIORIDADE_TAMANHO.get(item[2], 99),  # 2º critério: Tamanho (P, M, G)
            item[0],                         # 3º critério: Nome ascendente
        ),
    )

def main():
    primeiro_caso = True

    while True:
        try:
            linha = input().strip()
            if not linha:
                continue

            n = int(linha)
            if n == 0:
                break

            pedidos = []
            for _ in range(n):
                nome = input().strip()
                cor, tamanho = input().split()
                pedidos.append((nome, cor, tamanho))

            # Separa os casos de teste por linha em branco
            if not primeiro_caso:
                print()
            primeiro_caso = False

            pedidos_ordenados = ordenar_camisetas(pedidos)
            for nome, cor, tamanho in pedidos_ordenados:
                print(f"{cor} {tamanho} {nome}")

        except EOFError:
            break

if __name__ == "__main__":
    main()
