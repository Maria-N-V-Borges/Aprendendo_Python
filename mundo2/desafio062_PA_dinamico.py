#Desafio: Gerador de PA dinâmico

print('=' * 40)
print(' GERADOR DE PA DINÂMICO')
print('=' * 40)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: ')) 

termo = primeiro
contador = 1
total = 0
mais = 10 # começamos mostrando 10 termos

while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo} ➡ ', end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print(f'Progresso finalizado com {total} termos mostrados')
