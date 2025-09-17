#Desafio: Programa para calcular preço de passagem

d = float(input('Qual é a distância da viagem em Km '))

if d <= 200:
    p = d * 0.50
else:
    p = d * 0.45

print(f'O preço da passagem para {d:.1f}Km será de R${p:.2f} 💸')
