#Desafio: Programa para verificar se a pessoa tem "SILVA" no nome

n = input('Digite seu nome completo: ').strip()

tem_silva = 'SILVA' in n.upper()

if tem_silva:
    print('Sim! O nome contém SILVA')

else:
    print('Não, o nome não contém SILVA')
