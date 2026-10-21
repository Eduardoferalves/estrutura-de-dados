from math import gcd

def simplificar(num: int, den: int):
  """Reduz a fração e garante que o sinal negativo fique no numerador."""
  divisor = gcd(num, den)
  num_simp = num // divisor
  den_simp = den // divisor

  if den_simp < 0:
    num_simp = -num_simp
    den_simp = -den_simp

  return num_simp, den_simp

def calcular(n1: int, d1: int, op: str, n2: int, d2: int):
  """Executa a operação matemática indicada pelas regras do problema."""
  if op == '+':
    return (n1 * d2 + n2 * d1), (d1 * d2)
  if op == '-':
    return (n1 * d2 - n2 * d1), (d1 * d2)
  if op == '*':
    return (n1 * n2), (d1 * d2)
  if op == '/':
    return (n1 * d2), (d1 * n2)

# Leitura da quantidade de casos de teste
casos = int(input())

for _ in range(casos):
  # Desempacota a linha ignorando as barras '/'
  n1_str, _, d1_str, op, n2_str, _, d2_str = input().split()
  n1, d1, n2, d2 = map(int, [n1_str, d1_str, n2_str, d2_str])

  # 1. Calcula a fração original
  num, den = calcular(n1, d1, op, n2, d2)

  # 2. Calcula a fração simplificada
  num_simp, den_simp = simplificar(num, den)

  # 3. Exibe o formato exigido: "original = simplificado"
  print(f'{num}/{den} = {num_simp}/{den_simp}')