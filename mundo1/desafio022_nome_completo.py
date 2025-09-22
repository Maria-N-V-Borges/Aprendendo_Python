#Desafio: Programa para analisar o nome completo de uma pessoa

n = input('Digite seu nome completo: ').strip()

ma = n.upper()
mi = n.lower()

total_letras = len(n.replace(' ', ''))

primeiro_nome = n.split()[0]
letras_primeiro = len(primeiro_nome)

print(f'Nome em maiúscula: {ma}')
print(f'Nome em minúsculas: {mi}')
print(f'Total de letras (sem espaços): {total_letras}')
print(f'O primeiro nome é {primeiro_nome} e ele tem {letras_primeiro} letras')


#.strip() remove espaços extras no inicio e no fim
#.upper() deixa tudo MAIÚSCULO
#.lower() deixa tudo minúsculo
#.replace(' ','') remove os espaços pra conter só as letras
#.split()[0] pega a primera palavra do nome, ou seja, o primeiro nome.
