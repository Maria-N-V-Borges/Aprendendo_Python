"""
Calcula a área de um terreno retangular

Parâmetros:
- largura (float): Largura do terreno
- comprimento (float): Comprimento do terreno

Retorna:
- float: Área do terreno (largura * comprimento)
"""
def area(largura, comprimento):
  area = largura * comprimento
  return area

# programa principal
print("=" * 40)
print(f"{'CONTROLE DE TERRENOS':^40}")
print("=" * 40)

# Coletando dados com validação
while True:
  try:
    larg = float(input('LARGURA (m): '))
    if larg <= 0:
      print('ERRO! A largura deve ser maior que zero.')
      continue
    break
  except ValueError:
    print('ERRO! Digite um número válido.')

while True:
  try:
    comp = float(input('COMPRIMENTO (m): '))
    if comp <= 0:
      print('ERRO! O comprimento deve ser maior que zero.')
      continue
    break
  except ValueError:
    print('ERRO! Digite um número válido.')

# Chamando a função e mostrando o resultado
resultado = area(larg, comp)

print("=" * 40)
print(f'A área de um terreno {larg:.1f}x{comp:.1f} é de {resultado:.1f}m².')
print("=" * 40)
