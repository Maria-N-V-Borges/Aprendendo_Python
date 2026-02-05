def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        
        # Removemos o ponto para testar se o que sobrou é numérico
        if entrada.replace('.', '').isdigit():
            valido = True
            return float(entrada)
        else:
            print(f'\033[0;31mERRO: "{entrada}" é um preço inválido!\033[m')
