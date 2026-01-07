def voto(ano_nasc):
  from datetime import date # Importação local (boa prática em funções específicas)
  atual = date.today().year
  idade = atual - ano_nasc

  if idade < 16:
    return f'Com {idade} anos: NÃO VOTA'
  elif 16 <= idade < 18 or idade > 65:
    return f'Com {idade} anos: VOTO OPCIONAL'
  else:
    return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

#--- Programa principal ---
print("-" * 30)
nascimento = int(input("Em que ano você nasceu? "))
resultado = voto(nascimento)
print(resultado)
