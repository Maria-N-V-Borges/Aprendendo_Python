#Desafio: Programa para calcular o excesso de velocidade
v = float(input('Qual a velocidade do carro? '))

if v > 80:
    excesso = v - 80
    multa = excesso * 7
    print(f'Você foi multado! 🚨 Ultrapassou o limite em {excesso:.0f}Km/h')
    print(f'O valor da multa é R${multa:.2f}')
else:
    print('Parabéns 🥳! Você está dentro do limte de velocidade. Dirija com segurança 💖')

# O limite é 80 Km/h
# Se a velocidade for maior -> calcula o excesso
# Multa = excesso * 7
# Se não passar -> mensagem de parabéns
