#Desafio: Tabuada

n = int(input('Digite um número inteiro: '))

print(f'Tabuada de {n}: ')
for i in range(1,11):
    print(f'{n} x {i} = {n * i}')
