while True:
  n = int(input())
  if n == 0:
    break

  cartas = list(range(1, n + 1))
  descartadas = []
  inicio = 0

  # Executa enquanto houver 2 ou mais cartas restantes na fila
  while len(cartas) - inicio > 1:
    # 1. A carta do início é jogada fora
    descartadas.append(str(cartas[inicio]))

    # 2. A próxima carta vai para o final da fila
    cartas.append(cartas[inicio + 1])

    # 3. Avança o ponteiro de leitura em 2 posições
    inicio += 2

  # Monta a saída respeitando o formato exato
  texto_descarte = ", ".join(descartadas)
  print(
      f"Discarded cards: {texto_descarte}"
      if texto_descarte
      else "Discarded cards:"
  )
  print(f"Remaining card: {cartas[inicio]}")