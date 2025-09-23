while True:
    numero = int(input('Quer ver a tabuada de qual valor? (número negativo para parar): '))
    if numero < 0:
        print('\nPrograma encerrado. Obrigada por usa a tabuada 💖') 
        break

    print('-' * 30)
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')
    print('-' * 30)
