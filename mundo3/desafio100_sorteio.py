from random import randint
from time import sleep

numeros = []

def sorteia():
  print('Sorteando 5 valores da lista: ', end='')
  for i in range(5):
    n = randint(1, 10)
    numeros.append(n)
    print(n, end=' ')
    sleep(0.3)
  print('PRONTO!')

def somaPar():
    soma = 0
    for n in numeros:
      if n % 2 == 0:
        soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}')

sorteia()
somaPar()
