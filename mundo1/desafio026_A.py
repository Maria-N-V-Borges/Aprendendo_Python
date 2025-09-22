#Desafio: Programa que analisa a letra "A" em uma frase

f = input('Digite uma frase: ').strip().upper()
f_sem__espacos = f.replace(' ','')

q = f_sem__espacos.count('A')

p = f_sem__espacos.find('A') + 1

u = f_sem__espacos.rfind('A') + 1

print(f'A letra A aparece {q} vezes na frase.')
print(f'A primeira letra A aparece a posição {p}.')
print(f'A última letra A aparece na posição {u}.')

#.upper() → deixa tudo maiúsculo, pra não dar problema se a pessoa digitar a minúsculo.
#.count("A") → conta quantos “A” tem.
#.find("A") → pega a posição do primeiro “A”.
#.rfind("A") → pega a posição do último “A”.
#O +1 é só pra mostrar a posição de forma humana (começando em 1 e não em 0).
