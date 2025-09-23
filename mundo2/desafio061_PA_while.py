#Desafio: PA while

print('=' * 40)
print(' 10 TERMOS DE UM PROGRESSÃO ARITMÉTICA')
print('=' * 40)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: ')) 

termo = primeiro
contador = 1

while contador <= 10:
    print(f'{termo} ➡ ', end='')
    termo += razao
    contador += 1

print('FIM!')
