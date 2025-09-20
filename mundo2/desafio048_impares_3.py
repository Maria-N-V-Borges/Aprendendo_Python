#Desafio: Programa para somar os ímpares múltiplos de 3 entre 1 e 500

soma = 0
contador = 0

for num in range(1, 501, 2): # Só pega os números ímpares
    if num % 3 == 0: # verifica se é multiplo de 3
        soma += num
        contador += 1
    
print(f'A soma de todos os {contador} valores é {soma}')

#soma += num ->  vai acumular a soma
# contador += -> só pra contar quantos números entraram na soma
