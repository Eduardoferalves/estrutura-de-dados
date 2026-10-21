# Tabela direta de precedência (o '(' com peso 0 evita checagens extras)
PRECEDENCIA = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

def infixa_para_posfixa(expressao: str) -> str:
  pilha = []
  saida = []

  for c in expressao:
    # 1. Se for operando (letra ou número), vai direto para a saída
    if c.isalnum():
      saida.append(c)

    # 2. Início de subexpressão
    elif c == "(":
      pilha.append(c)

    # 3. Fim de subexpressão: desempilha tudo até achar o '('
    elif c == ")":
      while pilha and pilha[-1] != "(":
        saida.append(pilha.pop())
      pilha.pop()  # Descarta o '(' da pilha

    # 4. Operador (+, -, *, /, ^)
    else:
      # Desempilha operadores que têm prioridade maior ou igual à dele
      while pilha and PRECEDENCIA[pilha[-1]] >= PRECEDENCIA[c]:
        saida.append(pilha.pop())
      pilha.append(c)

  # 5. Despeja o restante dos operadores que sobraram na pilha
  while pilha:
    saida.append(pilha.pop())

  return "".join(saida)

# Leitura dos casos
n = int(input())
for _ in range(n):
  expr = input().strip()
  print(infixa_para_posfixa(expr))