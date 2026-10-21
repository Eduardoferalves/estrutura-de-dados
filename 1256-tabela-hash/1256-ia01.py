def simular_tabela_hash(m: int, chaves: list[int]) -> list[str]:
    """
    Simula uma Tabela Hash com M endereços-base e tratamento de colisões
    por encadeamento exterior (separate chaining).
    Retorna a representação visual formatada de cada lista da tabela.
    """
    # Inicializa os M compartimentos (buckets) como listas vazias
    tabela: list[list[int]] = [[] for _ in range(m)]

    # Insere as chaves nos respectivos endereços calculados pela função de dispersão h(x) = x % M
    for chave in chaves:
        endereco = chave % m
        tabela[endereco].append(chave)

    linhas = []
    for i in range(m):
        # Constrói o encadeamento: índice -> chave1 -> chave2 -> ... -> \ (indicando NULL)
        elementos = [str(i)] + [str(val) for val in tabela[i]] + ["\\"]
        linhas.append(" -> ".join(elementos))

    return linhas

def main():
    casos = int(input().strip())

    for caso in range(casos):
        m, _ = map(int, input().split())
        chaves = list(map(int, input().split()))

        linhas = simular_tabela_hash(m, chaves)
        for linha in linhas:
            print(linha)

        # Imprime uma linha em branco separando os casos de teste
        if caso < casos - 1:
            print()

if __name__ == "__main__":
    main()
