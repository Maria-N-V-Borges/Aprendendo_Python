#Desafio: Programa para ler peso de 5 pessoas e mostrar o maior e o menor

maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}° pessoa (em Kg): '))

    if i == 1: # se for o primeiro peso, inicializa maior e menor
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'\n O maior peso lido for {maior} Kg')
print(f'O menor peso lido foi {menor} kg')

# Começamos com maior e menor valendo 0, mas cuidado: Se você comparar direto com 0, 
# pode dar problema (imagine todo mundo com peso maior que 0)
# por isso no primeiro laço (i == 1), eu já guardo o primeiro peso em maior e menor.
# Depois, a cada nova entrada:
# Se for maior que maior, atualiza
# Se for menor que menor, atualiza
# No final mostrando o maior e o menor
