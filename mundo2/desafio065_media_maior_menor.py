soma = 0
quantidade = 0
maior = menor = 0

while True:
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1

    if quantidade == 1: # primeiro número digitado
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    
    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break

media = soma / quantidade
print(f'\nVocê digitou {quantidade} números')
print(f'A média dos valores é {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
