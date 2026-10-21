# Diretrizes para Assistentes de IA (AGENTS.md)

Este repositório contém exercícios e resoluções da disciplina de **Algoritmos e Estrutura de Dados** em Python.

## 🎯 Objetivo Principal
O objetivo deste repositório é servir como base sólida de preparação para as **Avaliações Práticas**.
A referência técnica mais valiosa do repositório são os arquivos terminados em `-aula.py` (resoluções feitas pelo professor em sala de aula).

---

## 📌 Convenção da Estrutura de Pastas
- `[numero]-[tema]/[numero]-aula.py`: Solução feita em aula com o professor. É a referência do estilo esperado nas provas práticas.
- `[numero]-[tema]/[numero]-ia01.py`: Resolução alternativa gerada por IA. Deve ser simples, eficiente, modular e bem documentada.
- `[numero]-[tema]/[numero].png`: Imagem com enunciado completo, restrições e exemplos de Entrada/Saída (Beecrowd/URI).
- Pastas com sufixo `-exercicio`: Exercícios propostos para treino extraclasse (sem resolução de aula prévia). A IA deve ler o enunciado em `.png` e resolver seguindo o estilo do professor.

---

## 🛠️ Padrões de Código e Estilo do Professor
Ao gerar ou explicar códigos para este repositório, siga estritamente estes padrões:

1. **Objetividade e Simplicidade:** Não utilize classes ou abstrações complexas a menos que o problema conceitualmente exija (ex: `class No` para listas encadeadas). Prefira funções diretas e procedimentos limpos.
2. **Biblioteca Padrão:** Use apenas recursos nativos (`collections.deque`, `heapq`, `math`, `sys`, `itertools`).
3. **Pilha:** `list` nativa com `.append()` e `.pop()`.
4. **Fila FIFO:** `collections.deque` com `.append()` e `.popleft()`.
5. **Fila de Prioridade:** `heapq` com `-valor` para priorizar o maior elemento (Max-Heap).
6. **Tabela Hash:** Lista de baldes `tabela = [[] for _ in range(M)]` com dispersão `valor % M` e encadeamento exterior.
7. **Ordenação com Lambda:** `.sort(key=lambda x: (...))` com tuplas para múltiplos critérios.
8. **Estruturas Circulares:** Operador módulo `(pos + passos) % n`.
9. **Entrada e Saída:** `input().split()` e tratamento de EOF com `try: ... except EOFError: break` ou `sys.stdin.read().split()`.
