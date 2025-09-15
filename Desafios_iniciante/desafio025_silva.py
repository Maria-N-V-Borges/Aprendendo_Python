#Desafio: Programa para verificar se a pessoa tem "SILVA" no nome

n = input('Digite seu nome completo: ').strip()

tem_silva = 'SILVA' in n.upper()

if tem_silva:
    print('Sim! O nome contém SILVA')

else:
    print('Não, o nome não contém SILVA')

#.strip() → tira espaços antes e depois.
#.upper() → deixa tudo maiúsculo pra evitar erro de digitar “Silva”, “silva” ou “SILVA”.
#"SILVA" in nome.upper() → verifica se “SILVA” aparece em qualquer parte do nome.
