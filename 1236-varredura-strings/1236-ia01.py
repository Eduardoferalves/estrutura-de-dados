from itertools import groupby
import sys

def compactar_linha(texto: str) -> str:
    """
    Compacta sequências repetidas de zeros ('0') e espaços (' ') maiores ou iguais a 3:
    - Zeros repetidos são codificados com '#' seguido pelo caractere ASCII da quantidade.
    - Espaços repetidos são codificados com '$' seguido pelo caractere ASCII da quantidade.
    - Blocos maiores que 255 são divididos em múltiplos de 255.
    - Sequências com 1 ou 2 ocorrências e outros caracteres permanecem inalterados.
    """
    resultado = []
    # Mapeamento do caractere para o seu respectivo símbolo de compactação
    simbolos = {"0": "#", " ": "$"}

    # groupby agrupa caracteres idênticos consecutivos (Run-Length Encoding)
    for caractere, grupo in groupby(texto):
        quantidade = sum(1 for _ in grupo)

        if caractere in simbolos and quantidade >= 3:
            simbolo = simbolos[caractere]
            # Divide repetições em blocos de até 255 caracteres
            while quantidade > 255:
                resultado.append(simbolo)
                resultado.append(chr(255))
                quantidade -= 255

            resultado.append(simbolo)
            resultado.append(chr(quantidade))
        else:
            resultado.append(caractere * quantidade)

    return "".join(resultado)

def main():
    linhas = sys.stdin.read().splitlines()
    if not linhas:
        return

    quantidade_casos = int(linhas[0].strip())

    for idx in range(1, quantidade_casos + 1):
        if idx < len(linhas):
            print(compactar_linha(linhas[idx]))

if __name__ == "__main__":
    main()