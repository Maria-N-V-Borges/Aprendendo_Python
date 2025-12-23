times = (
    'Palmeiras', 'Internancional', 'Fluminense', 'Corinthians','Flamengo',
    'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG',
    'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 
    'Atlético-GO', 'Avaí', 'Chapecoense'
)

print('-=' * 30)

# a) os primeiros colocados
print(f'🔝 Os 5 primeiros colocados são: {times[0:5]}')

print('-=' * 30)

# b) Os últimos 4 colocados
print(f'🔻Os 4 últimos colocados são: {times[-4:]}')

print('-=' * 30)

# c) Times em ordem alfabética
print(f'📋 Times em ordem alfabética: {sorted(times)}')

print('-=' * 30)

# d) Posição da Chapecoense
posicao = times.index('Chapecoense') + 1
print(f'⚽ A Chapecoense está na {posicao}ª posição da tabela')
