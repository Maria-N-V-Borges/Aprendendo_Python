#Desafio: Programa para verificar se a cidade começa com "SANTO"

c = input('Digite o nome de uma cidade: ').strip()

comeca_com_santo = c.upper().startswith('SANTO')

if comeca_com_santo:
    print('Sim! A cidade começa com SANTO')

else:
    print('Não, a cidade não começa com SANTO')

#.strip() → tira espaços extras.
#.upper() → deixa tudo em maiúsculas pra não dar erro se a pessoa digitar “santo” ou “Santo”.
#.startswith("SANTO") → checa se a string começa com essa palavra.
