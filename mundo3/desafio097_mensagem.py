def escreva(msg):
  tamanho = len(msg) + 4 #conta quantos caracteres o texto tem
  # Espaço para: 2 espaços antes do texto, bordas laterais
  print('~' * tamanho)
  print(f'  {msg}')
  print('~' * tamanho)

escreva('Olá, Mundo!')
escreva('Python é incrível')
escreva('Maria está estudando função')
