jogador = {}
gols = []

jogador['nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range(1, partidas + 1):
  gols.append(int(input(f'Quantos gols na partida {i}? ')))

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
  print(f'{k.capitalize()}: {v}')

print('-=' * 30)
