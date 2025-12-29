matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 

for l in range(3):
  for c in range(3):
    matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))

print('-=' * 30)

for l in range(3):
  for c in range(3):
    print(f'[{matriz[l][c]:^5}]', end="") #Centraliza o número em 5 espaços para ficar bonito
  print()
