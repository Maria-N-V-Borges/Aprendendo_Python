#Desafio: Dobro, Triplo e Raiz Quadrada de um número

n = int(input('Digite um número: '))

dobro = n * 2
triplo = n * 3
raiz = n ** 0.5 

print(f'O número digitado foi {n}')
print(f'O dobro é {dobro}')
print(f'O triplo é {triplo}')
print(f'A raiz quadrada é {raiz:.2f}')

#n ** 0.5 é a forma rápida de calcular a raiz quadrada
#pow(n, 0.5) também funciona
#:.2f no final da f-string serve para mostrar a raiz com 2 casas decimais (ex: 4.00)
