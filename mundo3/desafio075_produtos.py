produtos = (
    'Lápis', 1.75, 
    'Borracha', 2.00, 
    'Caderno', 15.90,
    'Estojo', 9.50, 
    'Mochila', 120.00,
    'Caneta', 2.50
)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for i in range(0, len(produtos), 2):
  print(f'{produtos[i]:.<30}R$ {produtos[i + 1]:>7.2f}')
  
print('-' * 40)
