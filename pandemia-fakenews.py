# Algoritmo de contaminacao de noticias falsas.
# O usuario informa uma matriz quadrada populacional composta por numeros (0 ate 9), cerquilhas ('#') e pontos finais ('.').
#     - Os numeros retratam pessoas perigosas que espalham noticias falsas para as quatro direcoes cardiais. Seus valores representam o alcance da propagacao em cada direcao.
#     - As cerquilhas representam pessoas conscientes que identificam noticias falsas e interceptam-nas, encerrando sua difusao direcional.
#     - Os pontos finais sao regioes sem pessoas, mas nao impedem o fluxo de noticias falsas.
# Em seguida, o usuario escreve um par de coordenadas numericas.
# O algoritmo espalha uma noticia falsa na regiao das coordenadas fornecidas, iniciando uma propagacao recursiva de noticias falsas ao longo da matriz populacional.
# Sempre que uma pessoa perigosa recebe uma noticia falsa, ela a divulga e torna-se um 'X' na matriz.
# Ao final das propagacoes, o programa exibe a matriz populacional alterada.


# Funcao principal
def main():
    N = int(input())                                                                     # No. de linhas na matriz
    pop_mat = [input() for i in range(N)]                                                # Matriz populacao

    y, x = input().split()                                                               # Coordenadas (linha, coluna) = (y, x)

    # Conversao de string para inteiro
    x = int(x)
    y = int(y)

    pop_mat = infect(x, y, pop_mat)                                                      # Chamada da funcao de infeccao da populacao

    # Impressao da matriz pos-infeccao
    for row in pop_mat:
        print(row)



# Funcao principal recursiva de infeccao
def infect(x, y, matrix):
    if x < 0 or x > len(matrix[0]) - 1 or y < 0 or y > len(matrix) - 1:
        return matrix                                                                    # Caso as coordenadas (x, y) ultrapassem os limites da matriz, ela nao sofre alteracoes

    target = matrix[y][x]                                                                # Pessoa alvo da populacao

    # Condicao de alteracao (o alvo deve ser numerico para ser infectado)
    if target in '0123456789':
        intensity = int(target)                                                          # Nivel de intensidade (convertido para inteiro)
        matrix[y] = matrix[y][0:x] + 'X' + matrix[y][x + 1:]                             # Fatiamento da linha y para que o alvo a ser infectado seja marcado por X

        matrix = horizontal_infection(matrix, x, y, intensity)                           # Propagacao horizontal da infeccao
        matrix = vertical_infection(matrix, x, y, intensity)                             # Propagacao vertical da infeccao

    return matrix                                                                        # Retorno da matriz possivelmente alterada



# Funcao auxiliar de infeccao horizontal
def horizontal_infection(matrix, x, y, num):

    # -------------------- Infeccao para direita --------------------

    for i in range(1, num + 1):
        if x + i > len(matrix[0]) - 1 or matrix[y][x + i] == '#':
            break                                                                        # Se a propagacao chegar ao limite da matriz ou a um #, ela eh interrompida

        matrix = infect(x + i, y, matrix)                                                # Chamada recursiva (indireta) da funcao

    # -------------------- Infeccao para esquerda -------------------

    for i in range(1, num + 1):
        if x - i < 0 or matrix[y][x - i] == '#':
            break                                                                        # Se a propagacao chegar ao limite da matriz ou a um #, ela eh interrompida

        matrix = infect(x - i, y, matrix)                                                # Chamada recursiva (indireta) da funcao

    # ---------------------------------------------------------------

    return matrix                                                                        # Retorno da matriz possivelmente alterada na horizontal



# Funcao auxiliar de infeccao vertical
def vertical_infection(matrix, x, y, num):

    # ---------------------- Infeccao para cima ---------------------

    for i in range(1, num + 1):
        if y + i > len(matrix) - 1 or matrix[y + i][x] == '#':
            break                                                                        # Se a propagacao chegar ao limite da matriz ou a um #, ela eh interrompida

        matrix = infect(x, y + i, matrix)                                                # Chamada recursiva (indireta) da funcao

    # -------------------- Infeccao para baixo ----------------------

    for i in range(1, num + 1):
        if y - i < 0 or matrix[y - i][x] == '#':
            break                                                                        # Se a propagacao chegar ao limite da matriz ou a um #, ela eh interrompida

        matrix = infect(x, y - i, matrix)                                                # Chamada recursiva (indireta) da funcao

    # ---------------------------------------------------------------

    return matrix                                                                        # Retorno da matriz possivelmente alterada na horizontal



if __name__ == '__main__':
    main()                                                                               # A funcao principal eh chamada somente se o programa eh executado como script

