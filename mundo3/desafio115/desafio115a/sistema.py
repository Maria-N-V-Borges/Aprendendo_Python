from lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])

    if resposta == 1:
        cabecalho('Opção 1 - Ver Pessoas')
    elif resposta == 2:
        cabecalho('Opcao 2 - Cadastrar Pessoas')
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1.5)
