valores = (
    int(input('Digite o primeiro valor: ')),
    int(input('Digite o segundo valor: ')),
    int(input('Digite o terceiro valor: ')),
    int(input('Digite o quarto valor: '))
)

print('-=' * 30)

# a) Quantas vezes apareceu o valor 9
print(f'O valor 9 apareceu {valores.count(9)} vez(es).')

print('-=' * 30)

# b) Em que posição foi digitado o primeiro valor 3
if 3 in valores:
  print(f'O valor 3 apareceu na {valores.index(3) + 1}ª posição.')
else:
  print('O valor 3 não foi digitado em nenhuma posição.')

print('-=' * 30)

# c) Quais foram os números pares
print('Os valores pares digitados foram:', end=' ')
for n in valores:
  if n % 2 == 0:
    print(n, end=' ')
