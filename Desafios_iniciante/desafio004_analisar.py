#Desafio: Programa para analisar uma entrada de teclado

algo = input('Digite algo: ')

print(f'O tipo primitivo desse valor é: {type(algo)}')
print(f'Só tem espaços? {algo.isspace()}')
print(f'É um número? {algo.isnumeric()}')
print(f'É um alfabético? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Está em maiúscula? {algo.isupper()}')
print(f'Está em minúscula? {algo.islower()}')
print(f'Está capitalizado (primeira letra maiúscula)? {algo.istitle()}')
