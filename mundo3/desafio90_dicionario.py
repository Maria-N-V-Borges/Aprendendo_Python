aluno = {}

aluno['nome'] = input('Nome do aluno: ')
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
  aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5:
  aluno['situacao'] = 'Recuperação'
else:
  aluno['situacao'] = 'Reprovado'

print('-=' * 30)

for chave, valor in aluno.items(): #.items() permite percorrer chave e valor juntos
  print(f'{chave.capitalize()}: {valor}')
