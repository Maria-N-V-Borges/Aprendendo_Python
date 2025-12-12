soma = 0
quantidade = 0

while True:
    numero = int(input('Digite um número (999 para parar): '))

    if numero == 999:
        break

    soma += numero
    quantidade += 1

print(f'\nVocê digitou {quantidade} números')
print(f'A soma entre eles é {soma}.')

#While true: cria um laço infinito
#if numero == 999: verifica o flag para parar
# soma += numero aculuma valores
# quantidade += 1 conta quantos números foram digitados
# No final, mostramos tudo com f-string
