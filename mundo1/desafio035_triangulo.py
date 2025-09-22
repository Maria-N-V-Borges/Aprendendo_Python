#Desafio: Programa para verificar se três retas formam um triângulo

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

if a + b > c and a + c > b and b + c > a:
    print('Sim! As retas podem formar um triângulo 💖')
else:
    print('Não, as retas NÃO formar um triângulo 😅')

# Para três retas formarem um triângulo, a soma de dois lados deve ser maior que o terceiro, para todas as combinações:
# a + b > c
# a + c > b
# b + c > a
# Se todas foram verdadeiras -> triângulo existe
