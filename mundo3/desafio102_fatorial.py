def fatorial(n, show=False):
  """
  Calcula o fatorial de um número.
  Parâmetros:
  n (int): Número a ser calculado (deve ser >= 0)
  show (bool, opcional): Mostrar ou não o processo de cálculo
                          Padrão é False (não mostrar).
  Retorna:
  int: O valor do fatorial de n.
  """
  if n < 0:
    raise ValueError("Fatorial não definido para números negativos")

  # Edge case for 0! and 1!
  if n == 0 or n == 1:
    resultado = 1
    if show:
      if n == 0:
        print("0! = 1")
      else:
        print("1! = 1")
    return resultado # Return here to avoid further calculation

  # Cálculo do fatorial
  resultado = 1
  expressao = [] # Para armazenar os passos se show=True

  for i in range(n, 0, -1):
    resultado *= i # Fixed: Changed '1' to 'i' in the multiplication
    if show:
      expressao.append(str(i))

  # Mostra o processo se solicitado
  if show:
    # Junta os números com ' x '
    processo = " x ".join(expressao)
    print(f"{n}! = {processo} = {resultado}")

  return resultado

# Programa principal
print("-=" * 50)
print(f"{'CALCULADORA DE FATORIAL':^50}")
print("-=" * 50)

# Testando a função
while True:
  try:
    num = int(input("Digite um número para calcular o fatorial: "))
    if num < 0:
      print("Por favor, digite um número inteiro positivo.")
      continue

    mostrar = input("Deseja mostrar o processo de cálculo? [S/N] ").strip().upper()
    show_param = mostrar == 'S'

    print("\n" + "-" * 30)

    # Chamado a função
    resultado = fatorial(num, show_param)

    if not show_param:
      print(f"O fatorial de {num}! = {resultado}")

    print("-" * 30)

    #Pergunta se quer continuar
    continuar = input("Deseja calcular outro fatorial? [S/N] ").strip().upper()
    if continuar != 'S':
      break

  except ValueError as e:
    print(f"Erro: {e}")
  except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

print("\n" + "=" * 50)
print(f"{'PROGRAMA ENCERRADO':^50}")
print("=" * 50)
