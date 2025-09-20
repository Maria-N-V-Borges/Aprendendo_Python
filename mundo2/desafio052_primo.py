#Desafio: Programa para verificar se um número é primo

num = int(input('Digite um número inteiro: '))
divisores = 0

for c in range(1, num + 1):
    if num % c == 0: #verifica se o número é divisível por c
        divisores += 1 #Se for, soma 1 no contador divisores

if divisores == 2: #Se tiver apenas 2 divisores (1 e ele mesmo) -> primo
    print(f'O número {num} é PRIMO 💖')
else:
    print(f'O número NÃO é primo 😅')
