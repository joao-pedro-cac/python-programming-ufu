# Jogo de "Avatar: A Lenda de Aang" sobre treinamento de manipulação elemental.
# O usuário constantemente informa um elemento e atribui-lhe valor arbitrário, e o elemento oposto tem seu número subtraído pela metade do valor informado.
# Os pares de elementos opostos são ÁGUA / FOGO e TERRA / AR.
# Ao informar 'X' como elemento, o programa se encerra, mostrando os resultados numéricos finais de cada elemento.


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
