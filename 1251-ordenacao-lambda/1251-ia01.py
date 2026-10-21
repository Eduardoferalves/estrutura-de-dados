from collections import Counter
import sys

def ordenar_frequencias_caracteres(texto: str) -> list[tuple[int, int]]:
    """
    Contabiliza a frequência dos caracteres pelo código ASCII e ordena conforme a regra:
    1. Ordem ascendente de frequência (frequência menor primeiro).
    2. Em caso de empate, ordem descendente do valor ASCII (-codigo).
    """
    # Mapeia cada caractere para seu valor ASCII e contabiliza ocorrências em O(N)
    frequencias = Counter(ord(char) for char in texto)

    # Ordenação multi-critério via tupla: (frequencia_crescente, codigo_decrescente)
    return sorted(frequencias.items(), key=lambda par: (par[1], -par[0]))

def main():
    # Lê todas as linhas da entrada padrão até o final do arquivo (EOF)
    linhas = sys.stdin.read().splitlines()
    if not linhas:
        return

    primeiro_caso = True

    for linha in linhas:
        # Garante a separação por linha em branco apenas entre os casos
        if not primeiro_caso:
            print()
        primeiro_caso = False

        resultado = ordenar_frequencias_caracteres(linha)
        for codigo_ascii, freq in resultado:
            print(f"{codigo_ascii} {freq}")

if __name__ == "__main__":
    main()