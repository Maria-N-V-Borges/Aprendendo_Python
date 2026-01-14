def leiaInt(msg):
  ok = False
  valor = 0
  while True:
    n = str(input(msg))
    if n.isnumeric():
      valor = int(n)
      ok = True
    else:
      print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    if ok:
      break
  return valor  

# --- PROGRAMA PRINCIPAL ---
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

# Cores no Terminal (\033[0;31m]): Usei código de escape ANSI para mostrar a mensagem de erro em vermelho.
# Lógica de Controle (ok = True): Usamos uma variável "bandeira" (flag) para saber quando o dado está correto e podemos sair do loop.
