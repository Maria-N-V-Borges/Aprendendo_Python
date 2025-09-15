#Desafio: Coverter reais em dólares

r = float(input('Quantos dinheiro você tem na carteira (R$)? '))

d = 5.20

quantidade_d = r / d

print(f'Com R${r:.2f} você pode comprar US${quantidade_d:.2f}')
