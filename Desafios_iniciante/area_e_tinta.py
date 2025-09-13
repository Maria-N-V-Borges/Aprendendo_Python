#Desafio: Programa para calcular área de parede e tinta necessária

l = float(input('Digite a largura da parede (em metros): '))
alt = float(input('Digite a altura da parede (em metros): '))

area = l * alt

litros_necessarios = area / 2

print(f'A área da parede é {area:.2f} m²')
print(f'Serão necessárias {litros_necessarios:.2f} litros de tinta para pintar a parede')

