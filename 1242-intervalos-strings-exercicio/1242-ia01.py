import sys

# Mapeamento das bases complementares alienígenas (B <-> S e C <-> F)
PARES_COMPLEMENTARES = {
    "B": "S",
    "S": "B",
    "C": "F",
    "F": "C",
}

def contar_ligacoes_rnaa(fita: str) -> int:
    """
    Calcula a quantidade máxima de ligações na fita de RNAA.
    Utiliza uma Pilha (Stack): cada nova base é comparada com a base no topo.
    Se forem complementares, ocorre uma dobra/ligação, desempilhando o topo;
    caso contrário, a base atual é empilhada para futuras potenciais dobras.
    Complexidade: O(N) tempo e O(N) espaço.
    """
    pilha: list[str] = []
    total_ligacoes = 0

    for base in fita:
        if pilha and pilha[-1] == PARES_COMPLEMENTARES.get(base):
            pilha.pop()
            total_ligacoes += 1
        else:
            pilha.append(base)

    return total_ligacoes

def main():
    linhas = sys.stdin.read().splitlines()
    if not linhas:
        return

    for linha in linhas:
        fita = linha.strip()
        if not fita:
            continue
        print(contar_ligacoes_rnaa(fita))

if __name__ == "__main__":
    main()