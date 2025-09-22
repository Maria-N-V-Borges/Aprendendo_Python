#Desafio: Menu de operações

print('✨ Bem vindo(a) ao menu de operações! ✨')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

opcao = 0

while opcao != 5:
    print('\nEscolha a operação:')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')

    opcao = int(input('Sua opção: '))

    if opcao == 1:
        print(f'A soma entre {n1} + {n2} = {n1 + n2}')
    elif opcao == 2:
        print(f'A multiplicação entre {n1} * {n2} = {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        elif n2 > n1:
            print(f'O maior número é {n2}')
        else:
            print('Os dois números são iguais')
    elif opcao == 4:
        n1 = int(input('Digite o novo primeiro número: '))
        n2 = int(input('Digite o novo segundo número: '))
    elif opcao == 5:
        print('Saindo do programa... Até mais!')
    else: 
        print('Opção inválida! Tente novamente')
