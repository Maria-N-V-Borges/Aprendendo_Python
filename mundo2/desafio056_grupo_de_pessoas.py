#Desafio: Programa para analisar grupo de pessoas

soma_idade = 0
homem_velho_nome = ''
homem_velho_idade = 0
mulheres_menor_20 = 0

for i in range(1, 5):
    print(f'\n-----{i}° PESSOA ------')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').strip().upper()

    soma_idade += idade

    if sexo == 'M':
        if idade > homem_velho_idade:
            homem_velho_idade = idade
            homem_velho_nome = nome
    
    if sexo == 'F' and idade < 20:
        mulheres_menor_20 += 1

media_idades = soma_idade / 4

print('\n====== Resultado ======')
print(f'A média de idade do grupo é {media_idades:.1f} anos')
if homem_velho_nome:
    print(f'O homem mais velho é {homem_velho_nome}, com {homem_velho_idade} anos')
else: 
    print('Não há homens no grupo')

print(f'Ao todo são {mulheres_menor_20} mulheres com menos de 20 anos')
