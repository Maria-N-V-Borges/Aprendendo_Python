#Desafio: Programa para (verificar se o ano é bissexto

from datetime import date

a = int(input('Digite um ano qualquer (Coloque 0 para analisar o ano atual): '))
if a == 0:
    a = date.today().year

if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print(f'O ano {a} é BISSEXTO! ✨🌙')
else:
    print(f'O ano {a} Não é bissexto. 🌺')

# Regra rápida do ano bissexto: É divisível por 4, mas não pode dividir por 100. A não ser que também divisível por 400.
# Ou seja, 2000 foi bissexto, mas 1900 não foi.
