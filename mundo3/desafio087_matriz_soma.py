matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

soma_pares = soma_terceira_coluna = maior_segunda_linha = 0

for l in range(3):
  for c in range(3):
    matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))

print('-=' * 30)

for l in range(3):
  for c in range(3):
    print(f'[{matriz[l][c]:^5}]', end="")
  print()

  # A) Soma dos valores pares
for l in range(3):
    for c in range(3):
     if matriz[l][c] % 2 == 0:
      soma_pares += matriz[l][c]

  # B) Soma da terceira coluna
for l in range(3):
    soma_terceira_coluna += matriz[l][2]

  # C) Maior valor da segunda linha
maior_segunda_linha = max(matriz[1])

print('-=' * 30)
print(f'A soma dos valores pares é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_segunda_linha}')
