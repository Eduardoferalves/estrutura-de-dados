while True:
  n = int(input())
  if n == 0:
    break

  entrada_a = input().split()
  saida_desejada = input().split()

  pilha = []
  movimentos = []
  ponteiro_b = 0  # Aponta para o próximo vagão esperado na saída

  for vagao in entrada_a:
    # 1. Insere o vagão na pilha (estação)
    pilha.append(vagao)
    movimentos.append("I")

    # 2. Enquanto o topo da pilha for o vagão esperado na saída, desempilha
    while pilha and pilha[-1] == saida_desejada[ponteiro_b]:
      pilha.pop()
      movimentos.append("R")
      ponteiro_b += 1

  # Junta os movimentos em uma string
  resultado = "".join(movimentos)

  # Se sobrou algum vagão na pilha, a sequência era impossível
  if pilha:
    print(f"{resultado} Impossible")
  else:
    print(resultado)