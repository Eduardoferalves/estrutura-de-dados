class NoCrianca:
    """Nó representando uma criança no círculo duplamente encadeado."""

    def __init__(self, nome: str, valor: int):
        self.nome = nome
        self.valor = valor
        self.anterior: "NoCrianca" = None
        self.proximo: "NoCrianca" = None

def simular_acampamento(dados_criancas: list[tuple[str, int]]) -> str:
    """
    Simula a dinâmica do círculo de crianças utilizando uma Lista Circular Duplamente Encadeada:
    - O próximo nó (proximo) representa o sentido anti-horário.
    - O nó anterior (anterior) representa o sentido horário.
    - Se o valor for ímpar, conta no sentido anti-horário.
    - Se o valor for par, conta no sentido horário.
    """
    total = len(dados_criancas)
    nos = [NoCrianca(nome, val) for nome, val in dados_criancas]

    # Conecta os nós formando um círculo bidirecional
    for i in range(total):
        nos[i].proximo = nos[(i + 1) % total]
        nos[i].anterior = nos[(i - 1) % total]

    atual = nos[0]
    valor_atual = atual.valor
    tamanho_atual = total

    while tamanho_atual > 1:
        # Otimiza o número de passos usando o módulo pelo tamanho atual do círculo
        passos = valor_atual % tamanho_atual
        if passos == 0:
            passos = tamanho_atual

        if valor_atual % 2 != 0:
            # Ímpar: avança no sentido anti-horário
            for _ in range(passos):
                atual = atual.proximo
        else:
            # Par: avança no sentido horário
            for _ in range(passos):
                atual = atual.anterior

        # 'atual' agora é a criança eliminada
        valor_atual = atual.valor
        no_ant = atual.anterior
        no_prox = atual.proximo

        # Remove o nó atual desvinculando-o da lista circular
        no_ant.proximo = no_prox
        no_prox.anterior = no_ant
        tamanho_atual -= 1

        # A contagem recomeça a partir do vizinho da criança recém-eliminada.
        # Ajustamos o ponteiro de partida para que o primeiro passo caia exatamente
        # no vizinho correto (no_prox se ímpar, no_ant se par).
        if valor_atual % 2 != 0:
            atual = no_ant
        else:
            atual = no_prox

    return atual.nome

def main():
    while True:
        try:
            linha = input().strip()
            if not linha:
                continue

            n = int(linha)
            if n == 0:
                break

            criancas = []
            for _ in range(n):
                nome, valor_str = input().split()
                criancas.append((nome, int(valor_str)))

            vencedor = simular_acampamento(criancas)
            print(f"Vencedor(a): {vencedor}")
        except EOFError:
            break

if __name__ == "__main__":
    main()