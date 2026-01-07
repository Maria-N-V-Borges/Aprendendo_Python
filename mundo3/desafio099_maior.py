def maior(*numeros):

  """
  Analisa vários valores inteiros e mostra qual é o maior.

  Parâmetros:
  - *numeros: Quantidade variável de valores inteiros.
  """
  print("-=" * 30)
  print('Analisando os valores passados...')

  if len(numeros) == 0:
    print('Foram informados 0 valores')
    print("Não existe maior valor")
    return None

  # Mostra todos os números
  print(f'Os valores informados foram: {len(numeros)} valores: ', end='')
  for num in numeros:
    print(f'{num} ', end='')
  print()

  # Encontra o maior
  maior_valor = numeros[0]
  for num in numeros:
    if num > maior_valor:
      maior_valor = num

  print(f'O maior valor informado foi {maior_valor}.')
  return maior_valor

# --- PROGRAMA PRINCIPAL ---
print("-=" * 50)
print('Desafio 099 - ENCONTRANDO O MAIOR VALOR'.center(50))
print("-=" * 50)

# Testando a função com diferentes quantidades de número
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

print("\n" + "=" * 50)
print(f"{'TESTES ADICIONAIS':^50}")
print("=" * 50)

#Outros testes
maior(10, 20, 30, 40, 50)
maior(-5, -10, -3, -1)
maior(100, 200, 150, 300, 250)
