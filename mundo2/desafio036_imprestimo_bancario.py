#Desafio: Programa para aprovar impréstimo bancário

valor_c = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual é o salário do comprador? R$ '))
a = int(input('Em quantos anos pretende pagar? '))

prestacao = valor_c / (a * 12)

limite = salario * 0.30

print(f'\nPara pagar a casa e, {a} anos, a prestação será de R${prestacao:.2f} por mês')

if prestacao <= limite:
    print('Empréstimo aprovado! 💖🏡')
else:
    print('Empréstimo negado 😅. A prestação ultrapassa 30% do salário')
