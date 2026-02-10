def leiaInt(msg):
    #Lê um número inteiro valido
    while True:
      try: 
         n = int(input(msg))
      except (ValueError, TypeError):
         print("\033[0;31mERRO: por favor, digite um número inteiro válido. \033[m")
         continue
      except KeyboardInterrupt:
         print("\n\033[0;31mEntrada interrompida pelo usuário.\033[m")
         return 0
      else:
         return n

def leiaFloat(msg):
   #Lè um número real (float) validado.
   while True:
      try:
         n = float(input(msg))
      except (ValueError, TypeError):
         print("\033[0;31mERRO: por favor, digite um número real válido.\033[m")
         continue
      except KeyboardInterrupt:
         print("\n\033[0;31mEntrada interrompda pelo usuário.\033[m")
         return 0.0
      else:
         return n
