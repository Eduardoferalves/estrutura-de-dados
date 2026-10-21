def contar_candidato(pos: int, passos: int, passo_direcao: int, ativos: list[bool]) -> int:
    """
    Avança no círculo na direção indicada (1 para horário, -1 para anti-horário)
    contando apenas os candidatos que ainda estão ativos.
    """
    total = len(ativos)
    while passos > 0:
        if ativos[pos]:
            passos -= 1
        if passos > 0:
            pos = (pos + passo_direcao) % total
    return pos

def simular_selecao(n: int, k: int, m: int) -> str:
    """
    Simula o processo de seleção circular com dois contadores:
    - Sentido horário contando k passos a partir da pessoa 1 (índice 0).
    - Sentido anti-horário contando m passos a partir da pessoa N (índice n - 1).
    """
    ativos = [True] * n
    restantes = n
    pos_horario = 0
    pos_anti_horario = n - 1

    resultados = []

    while restantes > 0:
        # Encontra os candidatos escolhidos por cada oficial
        escolhido_k = contar_candidato(pos_horario, k, 1, ativos)
        escolhido_m = contar_candidato(pos_anti_horario, m, -1, ativos)

        # As pessoas são numeradas de 1 a n
        p_k = escolhido_k + 1
        p_m = escolhido_m + 1

        if p_k == p_m:
            # Ambos selecionaram a mesma pessoa
            resultados.append(f"{p_k:3d}")
            ativos[escolhido_k] = False
            restantes -= 1
        else:
            # Selecionaram pessoas diferentes
            resultados.append(f"{p_k:3d}{p_m:3d}")
            ativos[escolhido_k] = False
            ativos[escolhido_m] = False
            restantes -= 2

        # Prepara a posição inicial para a próxima contagem
        pos_horario = (escolhido_k + 1) % n
        pos_anti_horario = (escolhido_m - 1) % n

    return ",".join(resultados)

def main():
    while True:
        try:
            linha = input().strip()
            if not linha:
                continue

            n, k, m = map(int, linha.split())
            if n == 0 and k == 0 and m == 0:
                break

            print(simular_selecao(n, k, m))
        except EOFError:
            break


if __name__ == "__main__":
    main()