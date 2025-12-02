#Para calcular seno, cosseno e tangente, usamos o módulo math.
#Mas atenção: a função sin, cos e tan usam radianos, não graus!
#Então precisamos converter usando radionas().

import math

angulo = float(input('Digite o ângulo em graus: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O ângulo de {angulo}° tem:')
print(f'Seno {seno:.4f}')
print(f'Cosseno {cosseno:.4f}')
print(f'Tangente {tangente:.4f}')
