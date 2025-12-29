pessoas = []
dados = []

maior = menor = 0

while True:
  dados.append(input('Nome: '))
  dados.append(float(input('Peso: ')))

  if len(pessoas) == 0:
    maior = menor = dados[1]
  else:
    if dados[1] > maior:
      maior = dados[1]
    if dados[1] < menor:
      menor = dados[1]

  pessoas.append(dados[:])
  dados.clear()

  resp = input('Quer continuar? [S/N] ').strip().upper()
  if resp == 'N':
    break

print('-=' * 30)

# A) Quantas pessoas foram cadasradas
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

# B) Lista com as pessoas mais pesadas
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
  if p[1] == maior:
    print(f'[{p[0]}]', end=' ')

print()

# C) Pessoas mais leves
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
  if p[1] == menor:
    print(f'[{p[0]}]', end=' ')
