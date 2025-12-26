valores = []

while True: #permite digitar quantos números quiser
  n = int(input('Digite um valor: '))

  if n not in valores: #not in: verifica se o número já existe na lista
    valores.append(n) #Append: Adiciona somente se for novo
    print('Valor adicionado com sucesso...')
  else:
    print('Valor duplicado! Não vou adicionar...')

  resp = input('Quer continuar? [S/N] ').strip().upper()
  if resp == 'N':
    break

valores.sort() #sort: ordena a lista em ordem crescente

print('-=' * 30)
print(f'Você digitou os valores: {valores}')
