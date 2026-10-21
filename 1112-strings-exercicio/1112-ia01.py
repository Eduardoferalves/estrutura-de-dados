import sys

class FenwickTree2D:
    """
    Árvore de Fenwick 2D (Binary Indexed Tree 2D):
    Permite atualizações pontuais e consultas de soma em regiões retangulares
    em tempo O(log X * log Y), ideal para grids dinâmicos de até 1000x1000.
    """

    def __init__(self, largura: int, altura: int):
        self.largura = largura
        self.altura = altura
        # Matriz 1-based para facilitar a manipulação de bits com LSB (i & -i)
        self.arvore = [[0] * (altura + 1) for _ in range(largura + 1)]

    def atualizar(self, x: int, y: int, valor: int):
        """Adiciona 'valor' à célula (x, y) (convertendo para 1-based)."""
        i = x + 1
        while i <= self.largura:
            j = y + 1
            while j <= self.altura:
                self.arvore[i][j] += valor
                j += j & (-j)
            i += i & (-i)

    def consulta_prefixo(self, x: int, y: int) -> int:
        """Retorna a soma de todas as células na região de (0, 0) até (x, y)."""
        soma = 0
        i = x + 1
        while i > 0:
            j = y + 1
            while j > 0:
                soma += self.arvore[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return soma

    def consulta_retangulo(self, x1: int, y1: int, x2: int, y2: int) -> int:
        """
        Retorna a soma dos elementos no retângulo delimitado por (x1, y1) e (x2, y2).
        Calcula os limites mínimos e máximos para suportar coordenadas em qualquer ordem.
        """
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        return (
            self.consulta_prefixo(max_x, max_y)
            - self.consulta_prefixo(min_x - 1, max_y)
            - self.consulta_prefixo(max_x, min_y - 1)
            + self.consulta_prefixo(min_x - 1, min_y - 1)
        )

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return

    idx = 0
    total_tokens = len(entrada)

    while idx < total_tokens:
        x_tam = int(entrada[idx])
        y_tam = int(entrada[idx + 1])
        preco = int(entrada[idx + 2])
        idx += 3

        if x_tam == 0 and y_tam == 0 and preco == 0:
            break

        q = int(entrada[idx])
        idx += 1

        bit2d = FenwickTree2D(x_tam, y_tam)

        for _ in range(q):
            tipo = entrada[idx]
            if tipo == "A":
                n = int(entrada[idx + 1])
                x = int(entrada[idx + 2])
                y = int(entrada[idx + 3])
                idx += 4
                bit2d.atualizar(x, y, n)
            elif tipo == "P":
                x = int(entrada[idx + 1])
                y = int(entrada[idx + 2])
                z = int(entrada[idx + 3])
                w = int(entrada[idx + 4])
                idx += 5

                total_schweisen = bit2d.consulta_retangulo(x, y, z, w)
                custo_total = total_schweisen * preco
                print(custo_total)

        # "Deixe uma linha em branco após cada caso de teste, inclusive após o último."
        print()

if __name__ == "__main__":
    main()