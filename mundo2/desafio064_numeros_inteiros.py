print('Digite vários números inteiros.')
print('Digite 999 para parar.\n')

soma = 0
quantidade = 0

while True: # Laço infinito, só quebra no "break"
    numero = int(input('Digite um número: '))
    if numero == 999: # condição de parada
        break
    soma += numero
    quantidade += 1

print(f'\nVocê digitou {quantidade} números.')
print(f'A soma entre eles é {soma}.')
