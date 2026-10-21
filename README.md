# Algoritmos e Estrutura de Dados

<p align="center">
  <img width="800" alt="Algoritmo e Estrutura de Dados" src="https://github.com/user-attachments/assets/7f23710b-c75c-4892-8a6b-f67c9185662e" />
</p>

Repositório dedicado ao estudo, prática e consolidação de exercícios da disciplina de **Algoritmos e Estrutura de Dados** em linguagem **Python**. 
Aqui estão reunidas as resoluções desenvolvidas em sala de aula, exercícios complementares e soluções alternativas focadas em clareza, eficiência e preparação para as **Avaliações Práticas**.

---

## 📅 Calendário de Avaliações
- **1ª Menção:** Avaliação Técnica — 09/10
- **2ª Menção:** Avaliação Prática — 30/10 🎯
- **3ª Menção:** Avaliação Técnica — 04/12
- **4ª Menção:** Avaliação Prática — 11/12 🎯

---

## 📁 Organização e Convenção do Repositório

Cada diretório do repositório corresponde a um problema do **Beecrowd/URI** e segue uma estrutura padrão:

```
[numero]-[tema]/
  ├── [numero]-aula.py   <- Resolução oficial feita em aula (estilo de referência para provas)
  ├── [numero]-ia01.py   <- Resolução alternativa criada por IA (modular, eficiente para estudo)
  └── [numero].png       <- Enunciado completo com regras, limites e casos de teste
```

> **Nota:** Pastas com sufixo `-exercicio` correspondem a exercícios propostos para prática extraclasse. Nelas, a resolução `*-ia01.py` foi construída rigorosamente no mesmo estilo e metodologia que o professor adota nas aulas.

---

## 🗺️ Índice Geral de Exercícios por Tópico

### 1. Pilhas (Stack - LIFO)
| Código | Exercício / Tema | Enunciado | Aula | IA (Alternativa) | Conceito Central |
|:---:|:---|:---:|:---:|:---:|:---|
| **1068** | [1068-pilha](./1068-pilha/) | [1068.png](./1068-pilha/1068.png) | [1068-aula.py](./1068-pilha/1068-aula.py) | [1068-ia01.py](./1068-pilha/1068-ia01.py) | Balanço de Parênteses com contador/pilha |
| **1069** | [1069-pilha-exercicio](./1069-pilha-exercicio/) | [1069.png](./1069-pilha-exercicio/1069.png) | *Exercício* | [1069-ia01.py](./1069-pilha-exercicio/1069-ia01.py) | Diamantes e Areia (extração de pares `<>`) |
| **1077** | [1077-pilha-notacao-matematica](./1077-pilha-notacao-matematica/) | [1077.png](./1077-pilha-notacao-matematica/1077.png) | [1077-aula.py](./1077-pilha-notacao-matematica/1077-aula.py) | [1077-ia01.py](./1077-pilha-notacao-matematica/1077-ia01.py) | Notação Infixa para Pós-fixa (Shunting-Yard) |
| **1242** | [1242-intervalos-strings-exercicio](./1242-intervalos-strings-exercicio/) | [1242.png](./1242-intervalos-strings-exercicio/1242.png) | *Exercício* | [1242-ia01.py](./1242-intervalos-strings-exercicio/1242-ia01.py) | RNA Alienígena (dobras e pares complementares) |

### 2. Filas (Queue - FIFO) e Listas Circulares
| Código | Exercício / Tema | Enunciado | Aula | IA (Alternativa) | Conceito Central |
|:---:|:---|:---:|:---:|:---:|:---|
| **1063** | [1063-fila-pilha-exercicio](./1063-fila-pilha-exercicio/) | [1063.png](./1063-fila-pilha-exercicio/1063.png) | *Exercício* | [1063-ia01.py](./1063-fila-pilha-exercicio/1063-ia01.py) | Transição de vagões entre Fila e Pilha |
| **1110** | [1110-fila](./1110-fila/) | [1110.png](./1110-fila/1110.png) | [1110-aula.py](./1110-fila/1110-aula.py) | [1110-ia01.py](./1110-fila/1110-ia01.py) | Descarte e envio para a base com `deque` |
| **1119** | [1119-fila-aplicada](./1119-fila-aplicada/) | [1119.png](./1119-fila-aplicada/1119.png) | [1119-aula.py](./1119-fila-aplicada/1119-aula.py) | [1119-ia01.py](./1119-fila-aplicada/1119-ia01.py) | Problema de Josephus com contadores horários/anti-horários |
| **1167** | [1167-fila-exercicio](./1167-fila-exercicio/) | [1167.png](./1167-fila-exercicio/1167.png) | *Exercício* | [1167-ia01.py](./1167-fila-exercicio/1167-ia01.py) | Lista Circular Duplamente Encadeada com módulo |

### 3. Fila de Prioridade (Heap) e Identificação de Estruturas
| Código | Exercício / Tema | Enunciado | Aula | IA (Alternativa) | Conceito Central |
|:---:|:---|:---:|:---:|:---:|:---|
| **1340** | [1340-fila-remocao-elementos](./1340-fila-remocao-elementos/) | [1340.png](./1340-fila-remocao-elementos/1340.png) | [1340-aula.py](./1340-fila-remocao-elementos/1340-aula.py) | [1340-ia01.py](./1340-fila-remocao-elementos/1340-ia01.py) | Identificação simultânea de Pilha, Fila e Max-Heap |

### 4. Tabelas Hash (Dispersão e Encadeamento)
| Código | Exercício / Tema | Enunciado | Aula | IA (Alternativa) | Conceito Central |
|:---:|:---|:---:|:---:|:---:|:---|
| **1256** | [1256-tabela-hash](./1256-tabela-hash/) | [1256.png](./1256-tabela-hash/1256.png) | [1256-aula.py](./1256-tabela-hash/1256-aula.py) | [1256-ia01.py](./1256-tabela-hash/1256-ia01.py) | Tabela Hash com função `x % M` e encadeamento exterior |

### 5. Algoritmos de Ordenação e Critérios com Lambda
| Código | Exercício / Tema | Enunciado | Aula | IA (Alternativa) | Conceito Central |
|:---:|:---|:---:|:---:|:---:|:---|
| **1025** | [1025-ordenacao-busca-binaria](./1025-ordenacao-busca-binaria/) | [1025.png](./1025-ordenacao-busca-binaria/1025.png) | [1025-aula.py](./1025-ordenacao-busca-binaria/1025-aula.py) | [1025-ia01.py](./1025-ordenacao-busca-binaria/1025-ia01.py) | Ordenação prévia e Busca Binária (ou Counting Sort) |
| **1162** | [1162-inversao](./1162-inversao/) | [1162.png](./1162-inversao/1162.png) | [1162-aula.py](./1162-inversao/1162-aula.py) | [1162-ia01.py](./1162-inversao/1162-ia01.py) | Contagem de trocas adjacentes (Insertion Sort / Bubble Sort) |
| **1244** | [1244-ordenacao-por-tamanho](./1244-ordenacao-por-tamanho/) | [1244.png](./1244-ordenacao-por-tamanho/1244.png) | [1244-aula.py](./1244-ordenacao-por-tamanho/1244-aula.py) | [1244-ia01.py](./1244-ordenacao-por-tamanho/1244-ia01.py) | Ordenação estável por tamanho (Bucket Sort $O(N)$) |
| **1251** | [1251-ordenacao-lambda](./1251-ordenacao-lambda/) | [1251.png](./1251-ordenacao-lambda/1251.png) | [1251-aula.py](./1251-ordenacao-lambda/1251-aula.py) | [1251-ia01.py](./1251-ordenacao-lambda/1251-ia01.py) | Ordenação por frequência e desempate por ASCII |
| **1258** | [1258-ordenacao-multiplos-criterios-lambda-exercicio](./1258-ordenacao-multiplos-criterios-lambda-exercicio/) | [1258.png](./1258-ordenacao-multiplos-criterios-lambda-exercicio/1258.png) | *Exercício* | [1258-ia01.py](./1258-ordenacao-multiplos-criterios-lambda-exercicio/1258-ia01.py) | Ordenação tripla (Cor crescente, Tamanho decrescente, Nome) |
| **1259** | [1259-inversao-exercicio](./1259-inversao-exercicio/) | [1259.png](./1259-inversao-exercicio/1259.png) | *Exercício* | [1259-ia01.py](./1259-inversao-exercicio/1259-ia01.py) | Pares crescentes e Ímpares decrescentes |

### 6. Strings e Varredura
| Código | Exercício / Tema | Enunciado | Aula | IA (Alternativa) | Conceito Central |
|:---:|:---|:---:|:---:|:---:|:---|
| **1087** | [1087-processamento-strings](./1087-processamento-strings/) | [1087.png](./1087-processamento-strings/1087.png) | [1087-aula.py](./1087-processamento-strings/1087-aula.py) | [1087-ia01.py](./1087-processamento-strings/1087-ia01.py) | Geometria de tabuleiro e movimentos da Dama |
| **1211** | [1211-strings](./1211-strings/) | [1211.png](./1211-strings/1211.png) | [1211-aula.py](./1211-strings/1211-aula.py) | [1211-ia01.py](./1211-strings/1211-ia01.py) | Economia de impressão e prefixo comum em strings |
| **1236** | [1236-varredura-strings](./1236-varredura-strings/) | [1236.png](./1236-varredura-strings/1236.png) | [1236-aula.py](./1236-varredura-strings/1236-aula.py) | [1236-ia01.py](./1236-varredura-strings/1236-ia01.py) | Run-Length Encoding com tabela ASCII |

### 7. Modelagem e Estruturas Avançadas
| Código | Exercício / Tema | Enunciado | Aula | IA (Alternativa) | Conceito Central |
|:---:|:---|:---:|:---:|:---:|:---|
| **1022** | [1022-modelagem-matematica](./1022-modelagem-matematica/) | [1022.png](./1022-modelagem-matematica/1022.png) | [1022-aula.py](./1022-modelagem-matematica/1022-aula.py) | [1022-ia01.py](./1022-modelagem-matematica/1022-ia01.py) | Operações com Frações e MDC (`math.gcd`) |
| **1023** | [1023-agrupamento](./1023-agrupamento/) | [1023.png](./1023-agrupamento/1023.png) | [1023-aula.py](./1023-agrupamento/1023-aula.py) | [1023-ia01.py](./1023-agrupamento/1023-ia01.py) | Agrupamento de consumo médio e truncamento |
| **1112** | [1112-strings-exercicio](./1112-strings-exercicio/) | [1112.png](./1112-strings-exercicio/1112.png) | *Exercício* | [1112-ia01.py](./1112-strings-exercicio/1112-ia01.py) | Árvore de Fenwick 2D (BIT 2D) para consultas retangulares |

---

## ⚡ Guia Rápido de Estruturas para a Prova Prática (Cheat Sheet)

Padrões recorrentes adotados pelo professor nas resoluções em aula:

### 1. Pilha (LIFO)
```python
pilha = []
pilha.append(elemento)  # Empilha
topo = pilha.pop()       # Desempilha (remove o último adicionado)
```

### 2. Fila (FIFO) com Deque
```python
from collections import deque

fila = deque()
fila.append(elemento)   # Enfileira no final
primeiro = fila.popleft() # Desenfileira do início em O(1)
```

### 3. Fila de Prioridade (Max-Heap) com Heapq
```python
import heapq

max_heap = []
heapq.heappush(max_heap, -valor)   # Inverte o sinal para simular Max-Heap
maior = -heapq.heappop(max_heap)    # Retira o maior valor em O(log N)
```

### 4. Tabela Hash com Encadeamento Exterior
```python
M = 13  # Número de endereços-base
tabela = [[] for _ in range(M)]

# Inserção
posicao = chave % M
tabela[posicao].append(chave)
```

### 5. Ordenação com Múltiplos Critérios (Lambda)
```python
# Exemplo: Ordena por frequência ascendente e desempata por valor descendente
elementos.sort(key=lambda x: (frequencia[x], -x))
```

### 6. Avanço Circular com Módulo
```python
pos = (pos + passos) % total_elementos
```

---

## 🤖 Integração com Assistentes de IA

Para apoiar os estudos com ferramentas de IA:
- **GitHub Copilot (VS Code):** Instruções personalizadas configuradas em `.github/copilot-instructions.md`.
- **IAs Gerais (Cursor, Claude, Gemini):** Regras do repositório definidas em `AGENTS.md`.
- Ambas as configurações instruem as ferramentas a priorizar a metodologia e as convenções adotadas pelo professor.
