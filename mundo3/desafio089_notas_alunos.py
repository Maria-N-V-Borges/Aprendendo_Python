alunos = []

while True:
  nome = input('Nome do aluno: ')
  nota1 = float(input('Nota 1: '))
  nota2 = float(input('Nota 2: '))

  media = (nota1 + nota2) / 2
  alunos.append([nome, [nota1, nota2], media])

  resp = input('Quer continuar? [S/N] ').strip().upper()
  if resp == 'N':
    break

print('-=' * 30)
print(f"{'No. ':<4}{'NOME':<10}{'MÉDIA':>8}")
print('-' * 26)

for i, aluno in enumerate(alunos):
  print(f"{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}")

print('-=' * 30)

while True:
  opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
  if opcao == 999:
    print('FINALIZANDO...❤️')
    break
  if opcao < 0 or opcao >= len(alunos):
    print('Aluno inválido! Tente novamente')
  else:
    print(f'Notas de {alunos[opcao][0]} são {alunos[opcao][1]}')
