dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram percorridos? '))

preco = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de R${preco:.2f}')
