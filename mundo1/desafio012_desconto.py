#Desafio: Clacular o preço com desconto

p = float(input('Digite o preço do produto: R$ '))

d = p * 0.05
novo_p = p - d

print(f'O preço original era R${p:.2f}')
print(f'Com 5% de desconto, o novo preço é R${novo_p:.2f}')

#Multiplicamos por 0.05 para calcular 5% do preço
#Subtraimos do valor original para obter o novo preço.
