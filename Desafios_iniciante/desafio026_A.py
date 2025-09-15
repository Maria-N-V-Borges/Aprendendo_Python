#Desafio: Programa que analisa a letra "A" em uma frase

f = input('Digite uma frase: ').strip().upper()

q = f.count('A')

p = f.find('A') + 1

u = f.rfind('A') + 1

print(f'A letra A aparece {q} vezes na frase.')
print(f'A primeira letra A aparece a posição {p}.')
print(f'A última letra A aparece na posição {u}.')
