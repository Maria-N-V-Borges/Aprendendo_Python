from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hip = hypot(co, ca)

print(f'A hipotenusa vai medir {hip:.2f}')

#hypot já faz: √(x² + y²)
#É mais limpo, mais seguro e mais preciso
