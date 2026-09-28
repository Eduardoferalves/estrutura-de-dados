from collections import deque
import heapq

while True:
    try:
        n = int(input())
    except EOFError:
        break

    pilha = []
    fila = deque()
    prioridade = []

    e_pilha = True
    e_fila = True
    e_prioridade = True

    for _ in range(n):
        operacao, valor = map(int, input().split())

        if operacao == 1:
            pilha.append(valor)
            fila.append(valor)
            heapq.heappush(prioridade, -valor)
        else:
            if not pilha or pilha.pop() != valor:
                e_pilha = False

            if not fila or fila.popleft() != valor:
                e_fila = False

            if not prioridade or -heapq.heappop(prioridade) != valor:
                e_prioridade = False

    possibilidades = sum([e_pilha, e_fila, e_prioridade])

    if possibilidades == 0:
        print("impossible")
    elif possibilidades > 1:
        print("not sure")
    elif e_pilha:
        print("stack")
    elif e_fila:
        print("queue")
    else:
        print("priority queue")