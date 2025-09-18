#Desafio: Programa para conversão de números

n = int(input('Digite um número inteiro: '))

print('\n' + 'Escolha a base de conversão:'.center(40,'='))
print('1 - binário'.center(40))
print('2 - Octal'.center(40))
print('3 - Hexadecimal'.center(40))
print('='*40)

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{n} em binário é {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} em octal é {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} em hexadecimal é {hex(n)[2:].upper()}')
else:
    print('Opção inválida 😅')

#bin(n) -> converte para binário (começa comm 0b)
#oct(n) -> converte para octal (começa com 0o)
#hex(n) -> converte para hexadecimal (começa com 0x)
#[2:] -> remove os prefixos 0b. 0o, 0x para deixar mais limpo
