total = 0
mais_1000 = 0
mais_barato = 0
nome_mais_barato = ' '

while True: 
    print('-' * 30)
    nome = input('Nome do produto: ').strip()
    preco = float(input('Preço: R$ '))

    total += preco

    if preco > 1000:
        mais_1000 += 1

    if mais_barato == 0 or preco < mais_barato:
        mais_barato = preco
        nome_mais_barato = nome
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break

print('\n======= RESUMO DA COMPRA =========')
print(f'Total gasto: R$ {total:.2f}')
print(f'Produtos que custam mais de R$1000: {mais_1000}')
print(f'Produto mais barato: {nome_mais_barato} (R$ {mais_barato:.2f})')
print('======================')
