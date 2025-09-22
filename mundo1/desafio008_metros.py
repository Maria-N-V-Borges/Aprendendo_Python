#Desafio: Programa para converter metros em centímetros e milímetros 

m = float(input('Digite o valor em metros: '))

c = m * 100
mi = m * 1000

print(f'{m} metros corresponde a {c} centímetros e {mi} milímetros')

#Multiplicamos por 100 para obter centímetros, porque 1 metro = 100 cm
#Miltiplicamos por 1000 para obter milímetros, porque 1 metro = 1000 cm
