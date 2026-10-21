from collections import deque
import heapq
import sys

def identificar_estrutura(operacoes: list[tuple[int, int]]) -> str:
    """
    Simula concomitantemente o comportamento de Pilha (LIFO), Fila (FIFO)
    e Fila de Prioridade (Max-Heap) para identificar a estrutura correspondente.
    """
    pilha: list[int] = []
    fila: deque[int] = deque()
    # Usamos valores negativos com heapq para simular uma Max-Heap (maior elemento sai primeiro)
    max_heap: list[int] = []

    pode_ser_pilha = True
    pode_ser_fila = True
    pode_ser_prioridade = True

    for op, valor in operacoes:
        if op == 1:
            # Operação de inserção
            if pode_ser_pilha:
                pilha.append(valor)
            if pode_ser_fila:
                fila.append(valor)
            if pode_ser_prioridade:
                heapq.heappush(max_heap, -valor)
        else:
            # Operação de remoção (op == 2)
            if pode_ser_pilha:
                if not pilha or pilha.pop() != valor:
                    pode_ser_pilha = False

            if pode_ser_fila:
                if not fila or fila.popleft() != valor:
                    pode_ser_fila = False

            if pode_ser_prioridade:
                if not max_heap or -heapq.heappop(max_heap) != valor:
                    pode_ser_prioridade = False

    total_validas = pode_ser_pilha + pode_ser_fila + pode_ser_prioridade

    if total_validas == 0:
        return "impossible"
    if total_validas > 1:
        return "not sure"
    if pode_ser_pilha:
        return "stack"
    if pode_ser_fila:
        return "queue"
    return "priority queue"

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return

    idx = 0
    total_tokens = len(entrada)

    while idx < total_tokens:
        n = int(entrada[idx])
        idx += 1

        operacoes = []
        for _ in range(n):
            op = int(entrada[idx])
            val = int(entrada[idx + 1])
            operacoes.append((op, val))
            idx += 2

        print(identificar_estrutura(operacoes))

if __name__ == "__main__":
    main()