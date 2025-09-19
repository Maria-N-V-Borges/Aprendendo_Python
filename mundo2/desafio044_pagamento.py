#Desafio: Programa de condições de pagamento

preco = float(input('Digite o preço do produto: R$ '))

print('\n' + 'Escolha a forma de pagamento:'.center(40,'='))
print('[1] À vista dinheiro/cheque (10% de desconto)'.center(40))
print('[2] Á vista no cartão (5% de desconto)'.center(40))
print('[3] Em até 2x no cartão (preço normal)'.center(40))
print('[4] 3x ou mais no cartão (20% de juros)'.center(40))
print('='*40)

opcao = int(input('Digite a opção: '))

if opcao == 1:
    total = preco * 0.90
    print(f'Pagamento à vista no dinheiro/cheque: R$ {total:.2f}')
elif opcao == 2:
    total = preco * 0.95
    print(f'Pagamento à vista no cartão: R$ {total:.2f}')
elif opcao == 3:
    parcela = preco / 2
    print(f'Pagamento em 2x no cartão: 2 parcelas de R$ {parcela:.2f} (total: R$ {preco:.2f})')
elif opcao == 4:
    total = preco * 1.20
    vezes = int(input('Quantas parcelas? '))
    parcela = total / vezes
    print(f'Pagamento em {vezes}x no cartão: {vezes} parcelas de R$ {parcela:.2f} (Total: R$ {total:.2f})')
else:
    print('Opção inválida. Tente novamente')
