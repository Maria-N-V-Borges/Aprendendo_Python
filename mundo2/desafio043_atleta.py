#Desafio: Programa para verificar a categoria de um atleta

from datetime import date

ano_nasc = int(input('Digite o ano de nascimento de alteta: '))

ano_atual = date.today().year

idade = ano_atual - ano_nasc

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Categoria: MIRIM 🐣')
elif idade <= 14:
    print('Categoria: INFATIL 🌟')
elif idade <= 19:
    print('Categoria: JÚNIOR ✨')
elif idade <= 20:
    print('Categoria: SÊNIOR 💪')
else:
    print('Categoria: MASTER 👑')
