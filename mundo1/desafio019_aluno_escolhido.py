import random

a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceiro aluno: ')
a4 = input('Nome do quarto aluno: ')

lista = [a1, a2, a3, a4]

escolhido = random.choice(lista)

print(f'O aluno escolhido para apagar o quadro foi {escolhido}')

#lista = [a1, a2, a3, a4] coloca todos os nomes detro de uma lista
#random.choice(lista) escolhe um nome aleatório
