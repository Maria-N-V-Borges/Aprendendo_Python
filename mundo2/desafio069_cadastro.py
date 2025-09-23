maiores_18 = 0
homens = 0
mulheres_menos_20 = 0

while True: 
    print('=-' * 20)
    print('CADASTRE UMA PESSOA')
    print('=-' * 20)

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()
    
    if idade >= 18:
        maiores_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]: ').strip().upper()

    if continuar == 'N':
        break

print('\n======== RESULTADOS ==========')
print(f'🔹 Pessoa com 18 anos ou mais: {maiores_18}')
print(f'🔹 Homens cadastrados: {homens}')
print(f'🔹 Mulheres com menos de 20 anos: {mulheres_menos_20}')
print('===================')

