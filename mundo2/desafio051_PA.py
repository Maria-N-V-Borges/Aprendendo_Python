#Desafio: Programa para PA

print('=== Progressão Aritmética ===')
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

termo = p
for i in range(1, 11):
    print(f'{termo}', end=' ➡ ')
    termo += r

print('Fim')
