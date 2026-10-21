import sys

def esta_balanceada(expressao: str) -> bool:
  saldo = 0

  for char in expressao:
    if char == "(":
      saldo += 1
    elif char == ")":
      saldo -= 1
      # Fechou parêntese sem ter nenhum aberto antes
      if saldo < 0:
        return False

  # Se o saldo for 0, todos os pares fecharam corretamente
  return saldo == 0

# Lê linha por linha até o fim da entrada (EOF) de forma limpa
for linha in sys.stdin:
  expressao = linha.strip()
  if not expressao:
    continue

  if esta_balanceada(expressao):
    print("correct")
  else:
    print("incorrect")