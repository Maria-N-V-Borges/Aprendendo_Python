palavras = (
    'python', 'programacao', 'estudar', 'aprender', 
    'computador', 'tecnologia', 'logica', 'dados'
)

for palavra in palavras:
  print(f'\nNa palavra {palavra.upper()} temos:', end=' ')
  
  for letra in palavra:
    if letra.lower() in 'aeiou':
      print(letra, end=' ')
