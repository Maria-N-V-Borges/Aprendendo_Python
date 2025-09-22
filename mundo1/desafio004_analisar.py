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

#type(algo) mostra o tipo do dado (mas cuidado: input() sempre lê como string).
#.isspace() → verifica se tem só espaços.
#.isnumeric() → diz se é só número.
#.isalpha() → diz se é só letras.
#.isalnum() → letras e números misturados.
#.isupper() / .islower() → maiúsculo ou minúsculo.
#.istitle() → se está como “Título” (primeira letra maiúscula).
