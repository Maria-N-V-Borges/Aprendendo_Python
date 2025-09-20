#Desafio: Programa para somar números pares

soma = 0

for i in range(1, 7): #6 números
    num = int(input(f'Digite o {i}° número: '))
    if num % 2 == 0: # verifica se é par
        soma += num # soma apenas os pares

print(f'A soma apenas dos números pares digitados é {soma}')
