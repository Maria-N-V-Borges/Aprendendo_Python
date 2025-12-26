valores = []

for i in range(5):
  n = int(input('Digite um valor: '))

  # if i == 0 ➡️ Se a lista estiver vazia, adiciona direto
  if i == 0 or n > valores[-1]: #[-1]: Se o número for maior que ele, vai pro final
    valores.append(n)
    print('Adicionado ao final da lista...')
  else:
    pos = 0
    while pos < len(valores):
      if n <= valores[pos]:
        valores.insert(pos, n) #While + insert(): Procura a posição correta e insere sem bagunçar a ordem
        print(f'Adicionado na posição {pos} da lista...')
        break
      pos += 1

print('-=' * 30)
print(f'Os valores digitados em ordem foram: {valores}')
