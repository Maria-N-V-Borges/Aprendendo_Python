#Desafio: fatorial

num = int(input('Digite um número para calcular o fatorial: '))
fatorial = 1

print(f'{num}! =', end=' ')

for i in range(num, 0, -1):
    fatorial *= i
    if i > 1:
        print(f'{i} x', end=' ')
    else:
        print(f'{i} =', end=' ')

print(fatorial)
