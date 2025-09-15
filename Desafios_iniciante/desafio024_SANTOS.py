#Desafio: Programa para verificar se a cidade começa com "SANTOS"

c = input('Digite o nome de uma cidade: ').strip()

comeca_com_santos = c.upper().startswith('SANTOS')

if comeca_com_santos:
    print('Sim! A cidade começa com SANTOS')

else:
    print('Não, a cidade não começa com SANTOS')

#.strip() → tira espaços extras.
#.upper() → deixa tudo em maiúsculas pra não dar erro se a pessoa digitar “santos” ou “Santos”.
#.startswith("SANTOS") → checa se a string começa com essa palavra.
