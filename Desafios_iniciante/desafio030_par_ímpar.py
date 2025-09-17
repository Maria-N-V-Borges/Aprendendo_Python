#Desafio: Programa para verificar se um número é par ou ímpar

n = int(input('Digite um número inteiro: '))

if n % 2 == 0:
    print(f'O número {n} é PAR 💖')
else: 
    print(f'O número {n} é ÍMPAR ✨')

# % é o resto da divisão
# Se n % 2 == 0, o resto é zero -> número é par.
# Caso contrário -> número ímpar
