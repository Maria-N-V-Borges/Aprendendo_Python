#Desafio: Programa para verificar se três retas formam um triângulo e o tipo

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

if a + b > c and a + c > b and b + c > a:
    print('Sim! As retas podem formar um triângulo 💖')

    if a == b == c:
        print('Tipo: Equilátero(Todos os lados iguais) ✨')
    elif a == b or a == c or b == c:
        print('Tipo: Isósceles (Dois lados iguais) 🌟')
    else: 
        print('Tipo: Escaleno (Todos os lados diferentes) ⭐')

else:
    print('Não, as retas NÃO formar um triângulo 😅')
