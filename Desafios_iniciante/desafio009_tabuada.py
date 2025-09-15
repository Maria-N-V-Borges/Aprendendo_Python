#Desafio: Tabuada

n = int(input('Digite um número inteiro: '))

print(f'Tabuada de {n}: ')
for i in range(1,11):
    print(f'{n} x {i} = {n * i}')

#range(1,11) cria número de 1 a 10
#for i in range (...) vai multiplicando o número que você digitou por cada i.
#f{n} x {i} = {n * i}' é só uma forma elegante de mostra o resultado.
