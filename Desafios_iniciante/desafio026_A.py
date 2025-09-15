#Desafio: Programa que analisa a letra "A" em uma frase

f = input('Digite uma frase: ').strip().upper()

q = f.count('A')

p = f.find('A') + 1

u = f.rfind('A') + 1

print(f'A letra A aparece {q} vezes na frase.')
print(f'A primeira letra A aparece a posição {p}.')
print(f'A última letra A aparece na posição {u}.')

#.upper() → deixa tudo maiúsculo, pra não dar problema se a pessoa digitar a minúsculo.
#.count("A") → conta quantos “A” tem.
#.find("A") → pega a posição do primeiro “A”.
#.rfind("A") → pega a posição do último “A”.
#O +1 é só pra mostrar a posição de forma humana (começando em 1 e não em 0).
