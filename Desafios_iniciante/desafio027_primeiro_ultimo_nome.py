#Desafio: Programa para mostrar primeiro e último nome

n = input('Digite seu nome completo: ').strip()

partes = n.split()

primeiro = partes[0]
u = partes[-1]

print(f'Primeiro nome: {primeiro}')
print(f'Último nome: {u}')

#.strip() → tira espaços extras no início e fim.
#.split() → divide o nome em uma lista (cada palavra vira um item).
#partes[0] → pega o primeiro item da lista (primeiro nome).
#partes[-1] → pega o último item da lista (último nome).
