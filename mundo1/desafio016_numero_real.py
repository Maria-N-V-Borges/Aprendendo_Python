from math import trunc

num = float(input('Digite um número real: '))
print(f'O número {num} tem a parte inteira {trunc(num)}.')

#O trunc() corta tudo depois da vírgula, sem arredondar
