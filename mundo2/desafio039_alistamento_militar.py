#Desafio: Programa para calcular o alistamento militar

from datetime import date

ano_atual = date.today().year

nasc = int(input('Digite o ano de nascimento: '))

idade = ano_atual - nasc

dif = 18 - idade

print(f'\nQuem nasceu em {nasc} tem {idade} anos em {ano_atual}.')

if idade < 18:
    print(f'Ainda não é hora de se alistar. Faltam {dif} anos')
elif idade == 18:
    print('Esta na hora de se alistar! ✨')
else:
    print(f'Já passou do tempo de alistamento. Passaram-se {abs(dif)} anos')

#abs -> O valor absoluto é sempre um número sem sinal. Se for positivo, continua positivo. 
#Se for negativo, ele tira o sinal e devolve positivo.
