#Desafio: Programa para verificar se uma frase é palíndromo

import unicodedata

def remover_acentos(txt):
    return ''.join(
        c for c in unicodedata.normalize('NFD', txt)
        if unicodedata.category(c) != 'Mn'
    )

frase = input('Digite uma frase: ').strip().upper()

frase_sem_espacos = remover_acentos(frase).replace(' ','')

inversa = frase_sem_espacos[::-1] # é um fatiamento que inverte a string toda

print(f'O inverso de {frase_sem_espacos} é {inversa}')

if frase_sem_espacos == inversa:
    print('Temos um PALÍNDROMO 💖')
else:
    print('A frase digitada NÃO é um palíndromo 😅')
