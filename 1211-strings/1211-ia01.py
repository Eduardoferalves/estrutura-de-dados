import sys

def prefixo_comum(str1: str, str2: str) -> int:
    """
    Retorna o número de caracteres coincidentes no prefixo entre duas strings.
    Interrompe a verificação no primeiro caractere diferente.
    """
    contagem = 0
    for c1, c2 in zip(str1, str2):
        if c1 == c2:
            contagem += 1
        else:
            break
    return contagem

def calcular_maxima_economia(telefones: list[str]) -> int:
    """
    Ordena os telefones lexicograficamente para aproximar os números com maiores
    prefixos comuns e calcula o total de caracteres economizados na impressão.
    """
    telefones.sort()
    economia = 0

    for i in range(1, len(telefones)):
        economia += prefixo_comum(telefones[i - 1], telefones[i])

    return economia

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return

    idx = 0
    total_tokens = len(entrada)

    while idx < total_tokens:
        n = int(entrada[idx])
        idx += 1

        telefones = entrada[idx : idx + n]
        idx += n

        print(calcular_maxima_economia(telefones))

if __name__ == "__main__":
    main()