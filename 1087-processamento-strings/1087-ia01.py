def movimentos_dama(x1: int, y1: int, x2: int, y2: int) -> int:
  dx = abs(x1 - x2)
  dy = abs(y1 - y2)

  # 0 movimentos: já está na casa de destino
  if dx == 0 and dy == 0:
    return 0

  # 1 movimento: mesma linha (dx == 0), mesma coluna (dy == 0) ou diagonal (dx == dy)
  if dx == 0 or dy == 0 or dx == dy:
    return 1

  # 2 movimentos: qualquer outra casa do tabuleiro
  return 2

while True:
  x1, y1, x2, y2 = map(int, input().split())

  # Condição de parada simplificada
  if x1 == y1 == x2 == y2 == 0:
    break

  print(movimentos_dama(x1, y1, x2, y2))