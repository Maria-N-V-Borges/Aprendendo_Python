print('=' * 40)
print('   CAIXA ELETRÔNICO')
print('=' * 40)

valor = int(input('Qual valor você quer sacar? R$ '))
resto = valor

celulas_50 = resto // 50
resto = resto % 50

celulas_20 = resto // 20
resto = resto % 20

celulas_10 = resto // 10
resto = resto % 10

celulas_1 = resto # O que sobrou são células de 1

print('\n=== Saque realizado ===')
if celulas_50 > 0: 
    print(f'{celulas_50} célula(s) de R$50')
if celulas_20 > 0:
    print(f'{celulas_20} célula(s) de R$20')
if celulas_10 > 0:
    print(f'{celulas_10} célula(s) de R$$10')
if celulas_1 > 0:
    print(f'{celulas_1} célula(s) de R$1')
print('===================')
