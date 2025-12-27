valores = []

while True:
  valores.append(int(input('Digite um valor: ')))

  resp = input('Quer continuar? [S/N] ').strip().upper()
  if resp == 'N':
    break

print('-=' * 30)

# A) Quantidade de números digitados
print(f'Você digitou {len(valores)} números.')

# B) Lista em ordem descrescente
valores.sort(reverse=True) #sort(reverse=True: Ordena do maior para o menor)
print(f'Os valores em ordem decrescente são: {valores}')

# C) Verificar se o número 5 está na lista
if 5 in valores:
  print('O valor 5 faz parte da lista!')
else:
  print('O valor 5 não faz parte da lista!')
