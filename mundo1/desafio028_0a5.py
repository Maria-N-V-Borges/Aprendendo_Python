import random
import time

#Desafio: Computador "pensa" em um número de 0 a 5
numero_pc = random.randint(0,5)

print('Vou pensar em um número entre 0 e 5... tente adivinhar! 🎲')
time.sleep(1) # pausa só pra dá um suspense

palpite = int(input('Qual número eu pensei? '))

if palpite == numero_pc:
    print(f'Parabéns 🥳! Você acertou, eu pensei no número {numero_pc} 💖')
else:
    print(f'Que pena 😅... eu pensei no número {numero_pc}, não no {palpite}.')

# import random -> pra gerar o número aleatório
# random.randint(0,5) -> escolhe um número inteiro de 0 até 5
# time.sleep(1) -> só pra criar um suspense
