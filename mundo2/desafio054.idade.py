#Desafio: Programa para verificar as idades

from datetime import date

maiores = 0
menores = 0
ano_atual = date.today().year

for i in range(1, 8):
    nascimento = int(input(f'Digite o ano de nascimento da {i}° pessoa: '))
    idade = ano_atual - nascimento
    if idade >= 21:
        maiores += 1
    else:
        menores += 1

print(f'\n Ao todo tivemos {maiores} pessoas MAIORES de idade')
print(f'E também tivemos {menores} pessoas MENORES de idade')
