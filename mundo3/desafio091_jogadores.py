from random import randint
from time import sleep
from operator import itemgetter

#Dicionário para armazenar os resultados
jogadores = {}

print('🎲 JOGANDO OS DADOS... 🎲')
print('-' * 30)

# Cada jogador joga o dado
for i in range(1, 5):
  jogadores[f'Jogador {i}'] = randint(1, 6)
  # Fixed: Changed f'jogador{i}' to f'Jogador {i}' to match the key used when storing the value
  print(f'O Jogador {i} tirou {jogadores[f'Jogador {i}']}')
  sleep(0.5) # pequena pausa para dar suspense

print('\n' + '=' * 30)
print(' RANKING DOS JOGADORES')
print('=' * 30)

# Ordenando o dicionário pelo valor (resultado do dado)
# Usamos itemgetter(1) para pegar o valor (não a chave)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

# Mostrando o ranking
for posicao, (nome, valor) in enumerate(ranking, start=1):
  print(f'{posicao}º lugar: {nome} com {valor} pontos')
  sleep(0.3)

print('\n' + '🏆' * 15)
print(f'PARABÉNS AO VENCEDOR: {ranking[0][0].upper()}')
print('🏆' * 15)
