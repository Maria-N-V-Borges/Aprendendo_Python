def aumentar(preco=0, taxa=0):
  """
  Retorna o preço aumentado pela taxa (%)
  """
  return preco + (preco * taxa / 100)

def diminuir(preco=0, taxa=0):
  """
  Retorna o preço diminuido pela taxa (%)
  """
  return preco - (preco * taxa / 100)

def dobro(preco=0):
  """
  Retorna o dobro do preço.
  """
  return preco * 2

def metade(preco=0):
  """
  Retorna a metade do preço.
  """
  return preco / 2
