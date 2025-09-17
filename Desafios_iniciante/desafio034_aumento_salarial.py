#Desafio: Programa para calcular aumento salarial

s = float(input('Qual é o salário de funcionário? R$ '))

if s > 1250:
    novo_s = s * 1.10 # aumento de 10%
else: 
    novo_s = s * 1.15 # aumento de 15%

print(f'Quem ganhava R${s:.2f} passa a ganhar R${novo_s:.2f} agora.')
