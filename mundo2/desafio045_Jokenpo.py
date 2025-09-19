#Desafio: Jokenpô

import random
import time

opcoes = ['Pedra', 'Papel', 'Tesoura']

print('Vamos jogar Jokenpô! 🎮')
print('[0] Pedra ✊')
print('[1] Papel 🤚')
print('[2] Tesoura ✌')

jogador = int(input('Escolha sua jogada: '))

computador = random.randint(0, 2)

print('JO...')
time.sleep(1)
print('KEN...')
time.sleep(1)
print('PÔ!!!\n')

print(f'Você jogou: {opcoes[jogador]}')
print(f'Computador jogou: {opcoes[computador]}')

if jogador == computador:
    print('Empate! 😅')
elif (jogador == 0 and computador == 2) or \
    (jogador == 1 and computador == 0) or \
    (jogador == 2 and computador == 1):
    print('Você venceu! 🥳')
else:
    print('Você perdeu! 😭')
