def moeda(valor=0, simbolo='R$'):
#Formata um número como valor monetário.
  return f'{simbolo}{valor:,.2f}'.replace(',', 'X').replace('.',',')

def aumentar(preco=0, taxa=0, formato=False):
#Retorna o preço aumentado pela taxa (%)
  res = preco + (preco * taxa / 100)
  return res if not formato else moeda(res)

def diminuir(preco=0, taxa=0, formato=False):
# Retorna o preço diminuido pela taxa (%)
  res = preco - (preco * taxa / 100)
  return res if not formato else moeda(res)

def dobro(preco=0, formato=False):
#Retorna o dobro do preço
  res = preco * 2
  return res if not formato else moeda(res)

def metade(preco=0, formato=False):
#Retorna a metade do preço
  res = preco / 2
  return res if not formato else moeda(res)

def resumo(preco=0, taxa_aumento=10, taxa_reducao=5):
# Exibe um resumo formatado com várias informações sobre o preço
  print('-' * 30)
  print('RESUMO DO VALOR'.center(30))
  print('-' * 30)
  print(f'Preço analisado: \t{moeda(preco)}')
  print(f'Dobro do preço: \t{dobro(preco, True)}')
  print(f'Metade do preço: \t{metade(preco, True)}')
  print(f'{taxa_aumento}% de aumento: \t{aumentar(preco, taxa_aumento, True)}')
  print(f'{taxa_reducao}% de redução: \t{diminuir(preco, taxa_reducao, True)}')
  print('-' * 30)
