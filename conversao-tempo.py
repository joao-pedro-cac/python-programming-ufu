# Joao Pedro Cavalcante Albuquerque Costa
# 12121ECP021


# Entrada do usuario
N = int(input())	# Segundos

# Conversao do tempo
m = N // 60               # Minutos
N %= 60

h = m // 60               # Horas
m %= 60

d = h // 24               # Dias
h %= 24


# Impressao do tempo convertido
print('{} dia(s), {} hora(s), {} minuto(s) e {} segundo(s).'.format(d, h, m, N))