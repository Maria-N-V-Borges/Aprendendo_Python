#Desafio: Programa para calcular o IMC

peso = float(input('Digita seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura ** 2)

print(f'Seu IMC é {imc:.2f}')

if imc < 18.5:
    print('Status: Abaixo do peso 😲')
elif imc < 25:
    print('Status: Peso ideal 😍')
elif imc < 30:
    print('Status: Sobrepeso 😬')
elif imc < 40:
    print('Status: Obesidade 😓')
else:
    print('Status: Obesidade mórbida 🚨')
    
