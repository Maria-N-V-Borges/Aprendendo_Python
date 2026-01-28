import moeda

preco = 100

print(f"Preço original: R$ {preco:.2f}")
print(f"Aumentado em 10%: R${moeda.aumentar(preco, 10): .2f}")
print(f"Diminuido em 20%: R${moeda.diminuir(preco, 20):.2f}")
print(f"O dobro: R${moeda.dobro(preco):.2f}")
print(f"A metade: R${moeda.metade(preco):.2f}")
