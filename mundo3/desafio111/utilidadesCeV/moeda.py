def moeda(valor=0, simbolo='R$'):
  return f"{simbolo}{valor:.2f}".replace('.', ',')

def aumentar(valor=0, taxa=0, formato=False):
  res = valor + (valor * taxa / 100)
  return moeda(res) if formato else res

def diminuir(valor=0, taxa=0, formato=False):
  res = valor - (valor * taxa / 100)
  return moeda(res) if formato else res

def dobro(valor=0, formato=False):
  res = valor * 2
  return moeda(res) if formato else res

def metade(valor=0, formato=False):
  res = valor / 2
  return moeda(res) if formato else res

def resumo(valor=0, taxa_aum=10, taxa_dim=5):
  print("-" * 30)
  print("RESUMO DO VALOR".center(30))
  print("-" * 30)
  print(f"Preço analisado: \t{moeda(valor)}")
  print(f"Dobro do preço: \t{dobro(valor, True)}")
  print(f"Metade do preço: \t{metade(valor, True)}")
  print(f"{taxa_aum}% de aumento: \t{aumentar(valor, taxa_aum, True)}")
  print(f"{taxa_dim}% de redução: \t{diminuir(valor, taxa_dim, True)}")
  print("-" * 30)
