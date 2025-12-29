numeros = [[], []] # numeros[0] = pares | numeros[1] = ímpares

for i in range(1, 8):
  n = int(input(f'Digite o {i}º valor: '))

  if n % 2 == 0:
    numeros[0].append(n)
  else:
    numeros[1].append(n)

numeros[0].sort() #sort(): Organiza cada lista em ordem crescente
numeros[1].sort()

print('-=' * 30)
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')
