# Joao Pedro Cavalcante Albuquerque Costa
# 12121ECP021


# Inicializacao das variaveis
element = ''                  # Elemento de treinamento

water = 0                     # Pontos de agua
fire = 0                      # Pontos de fogo
earth = 0                     # Pontos de terra
air = 0                       # Pontos de ar

# Laco de treinamento
while True:
  element = input()

  if (element == 'X'):        # Quebra de laco caso o usuario digite X
    break
  
  points = int(input())

  # Treinamento das habilidades
  if (element == 'W'):        # Agua
    water += points
    fire -= points / 2
    
  elif (element == 'F'):      # Fogo
    fire += points
    water -= points / 2
    
  elif (element == 'E'):      # Terra
    earth += points
    air -= points / 2
    
  else:                       # Ar (opcao por exclusao)
    air += points
    earth -= points / 2

  # Limitacao dos pontos para serem maiores que zero
  water = max(0, water)
  fire = max(0, fire)
  earth = max(0, earth)
  air = max(0, air)

  # Caso a pontuacao de um dado elemento seja menor que zero, a funcao max() retorna 0, limitando as pontuacoes para serem maiores ou iguais a zero


# Tabela de pontuacao
print('''Pontuacao Final
Agua: {:.1f}
Terra: {:.1f}
Fogo: {:.1f}
Ar: {:.1f}'''.format(water, earth, fire, air))

# Resposta final
if (water == 0 or earth == 0 or fire == 0 or air == 0):
  print("Realize mais treinamentos.")
  
else:
  print("Treinamento realizado com sucesso.")