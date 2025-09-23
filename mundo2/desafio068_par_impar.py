from random import randint

print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR 🎲')
print('=-' * 20)

vitorias = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    escolha = ' '

    while escolha not in 'PI':
        escolha = input('Par ou Ímpar? (P/I): ').strip().upper()
    
    print('-' * 40)
    print(f'Você jogou {jogador} e o computador {computador}. Total = {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 40)

    if (total % 2 == 0 and escolha == 'P') or (total % 2 == 1 and escolha == 'I'):
        print('✨🥳 Parabéns, você venceu! Vamos jogar de novo... 🥳✨')
        vitorias += 1
    else:
        print('Você perdeu! 😭\n')
        break

print(f'GAME OVER! Você conseguiu {vitorias} vitórias consecutivas 🏆')
