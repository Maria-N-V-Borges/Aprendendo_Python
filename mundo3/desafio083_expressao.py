expressao = input('Digite a expressão: ')

contador = 0

for simbolo in expressao:
  if simbolo == '(':
    contador += 1
  elif simbolo == ')':
    contador -= 1

    if contador < 0:
       break

if contador == 0:
  print('Sua expressão está correta!')

else:
  print('Sua expressão está incorreta!')
