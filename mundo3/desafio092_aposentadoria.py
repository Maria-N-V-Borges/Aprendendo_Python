from datetime import datetime

# Pegando o ano atual do sistema
ano_atual = datetime.now().year
dados = dict()

dados['nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = ano_atual - nascimento
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if dados['ctps'] != 0:
  dados['contratacao'] = int(input('Ano de contratação: '))
  dados['salario'] = float(input('Salário: R$'))

  # Cálculo de aponsetadoria:
  # Idade que tinha ao ser contratado + 35 anos de contrinuição
  idade_contratacao = dados['contratacao'] - nascimento
  dados['aposentadoria'] = idade_contratacao + 35

print('-=' * 30)
for k, v in dados.items():
  print(f' - {k} tem o valor {v}')
