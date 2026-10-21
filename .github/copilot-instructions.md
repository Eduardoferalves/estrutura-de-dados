# Instruções do Repositório — Algoritmos e Estrutura de Dados

Este repositório armazena exercícios práticos em Python da disciplina universitária de **Algoritmos e Estrutura de Dados**. 
O objetivo principal é a preparação para as **Avaliações Práticas** da disciplina.

---

## 1. Regra de Ouro: O Estilo do Professor

Em avaliações práticas, o critério mais valioso é o **estilo e a abordagem ensinados pelo professor em sala de aula**.
Sempre que você (Copilot) gerar código, tirar dúvidas ou sugerir implementações alternativas, siga rigorosamente as diretrizes abaixo:

1. **Simplicidade e Objetividade:**
   - Evite overengineering, padrões de projeto complexos ou classes desnecessárias.
   - Escreva código procedural, limpo, direto e de fácil leitura durante a prova.
   - Crie classes apenas quando a estrutura exigir conceitualmente (ex: `class No` para Lista Encadeada).

2. **Biblioteca Padrão Apenas:**
   - Use exclusivamente funções nativas e módulos da Standard Library do Python (`collections`, `heapq`, `math`, `sys`, `itertools`).

3. **Estruturas de Dados Padrão Ensinadas:**
   - **Pilhas (LIFO):** Utilize `list` nativa com `.append()` para empilhar e `.pop()` para desempilhar.
   - **Filas (FIFO):** Utilize `from collections import deque` com `.append()` para enfileirar e `.popleft()` para desenfileirar.
   - **Filas de Prioridade:** Utilize `import heapq`. Como o `heapq` implementa Min-Heap por padrão, inverta o sinal (`-valor`) quando precisar de uma Max-Heap (maior prioridade primeiro).
   - **Tabelas Hash:** Implemente com lista de baldes `tabela = [[] for _ in range(M)]`, função de dispersão `chave % M` e encadeamento exterior (separate chaining).
   - **Ordenação Multi-critério:** Utilize `.sort(key=lambda x: (...))` ou `sorted(...)` passando uma tupla de critérios (use `-valor` para inverter a ordem de desempate numérica).
   - **Estruturas Circulares:** Utilize aritmética modular `(pos + passos) % N` para avançar em listas ou ponteiros circulares.

4. **Entrada e Saída (Padrão Beecrowd / Maratona):**
   - Leitura de múltiplos inteiros: `map(int, input().split())`.
   - Casos até EOF: `while True: try: linha = input() ... except EOFError: break` ou `sys.stdin.read().split()`.
   - Saídas formatadas com delimitadores: `' '.join(...)` ou `' -> '.join(...)`.

---

## 2. Convenção de Arquivos do Repositório

Cada pasta representa um exercício/problema identificado pelo seu número no Beecrowd:

```
[numero]-[tema]/
  ├── [numero]-aula.py   <- Resolução oficial feita pelo professor em aula (referência máxima)
  ├── [numero]-ia01.py   <- Resolução alternativa criada por IA (modular, eficiente, para estudo)
  └── [numero].png       <- Imagem com o enunciado oficial do problema e exemplos de E/S
```

* **Pastas com sufixo `-exercicio`:** São exercícios complementares passados para praticar em casa (geralmente não contêm `*-aula.py`). Ao resolver exercícios nessas pastas, leia o enunciado em `*.png` e adote a abordagem que o professor utilizaria para aquele tema.
* Ao propor novas resoluções alternativas, salve como `*-ia01.py` (ou `*-ia02.py`), incluindo tipagem, docstring e explicações dos conceitos de Estrutura de Dados envolvidos.
