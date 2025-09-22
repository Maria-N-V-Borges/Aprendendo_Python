#Desafio: Jogo de adivinhação

import random

print('🎲 Bem-vindo(a) ao jogo de adivinhação! 🎲')
computador = random.randint(0,10) # computador "pensa" no número
palpites = 0
acertou = False

while not acertou:
    jogador = int(input('Tente adivinhar o número entre 0 e 10: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente novamente! 🎲')
        else: 
            print('Menos... tente novamente! 🎲')

print(f'💖Parabéns! 🥳 Você acertou o número {computador} em {palpites} tentativas!')
