caso = 1

while True:
  n = int(input())
  if n == 0:
    break

  # Linha em branco apenas ENTRE casos (o fim da saída não deve ter linha sobrando)
  if caso > 1:
    print()

  # Vetor de frequência: o índice é o consumo (0 a 200) e o valor é a soma de pessoas
  consumo_moradores = [0] * 201

  total_pessoas = 0
  total_consumo = 0

  for _ in range(n):
    moradores, consumo = map(int, input().split())
    total_pessoas += moradores
    total_consumo += consumo

    media_imovel = consumo // moradores
    consumo_moradores[media_imovel] += moradores

  # Monta a saída percorrendo de 0 a 200 (já sai ordenado crescentemente)
  resultado = []
  for c in range(201):
    if consumo_moradores[c] > 0:
      resultado.append(f"{consumo_moradores[c]}-{c}")

  # Truncamento exato de 2 casas decimais SEM arredondar (exige a regra do problema)
  inteiro = total_consumo // total_pessoas
  decimal = (total_consumo * 100 // total_pessoas) % 100

  print(f"Cidade# {caso}:")
  print(" ".join(resultado))
  print(f"Consumo medio: {inteiro}.{decimal:02d} m3.")

  caso += 1