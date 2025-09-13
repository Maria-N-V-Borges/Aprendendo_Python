#Desafio: Calcular aumento de salário

s = float(input('Digite o salário do funcionário: R$ '))

a = s * 0.15
novo_s = s + a

print(f'Salário original: R${s:.3f}')
print(f'Com 15% de aumento, o novo salário é R${novo_s:.3f}')
