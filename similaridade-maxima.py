# Jogo de similaridade.
# O usuario informa uma matriz 'n x n' e outra 'm x m' (m < n), ambas compostas exclusivamente por 0s e 1s.
# O algoritmo busca a submatriz 'm x m' da matriz maior que mais se assemelha a matriz menor.
# Ao fim, sua posicao na matriz maior e seu grau de similaridade com a matriz menor sao apresentados.


# Funcao principal
def main():
    # ------------------------- VARIAVEIS -------------------------
    dimG = int(input())                                                            # Dimensao da matriz grande
    matrizG = generateMatrix(dimG)                                                 # Criacao da matriz grande

    dimP = int(input())                                                            # Dimensao da matriz pequena
    matrizP = generateMatrix(dimP)                                                 # Criacao da matriz pequena

    pairs = []                                                                     # Lista de pares (POSICAO, GRAU DE SIMILARIDADE)

    # -------------------------- CALCULO --------------------------

    for row in range(dimG - dimP + 1):                                             # Laço para verificar as fileiras
        for column in range(dimG - dimP + 1):                                      # Laço para verificar as colunas (mais especificamente, os elementos de cada fileira)
            submatrizG = getSubmatrix(matrizG, row, column, dimP)                  # Recorte da matriz grande (submatriz) com mesma dimensao que a matriz pequena

            sim = getSim(submatrizG, matrizP)                                      # Calculo da similaridade entre a submatriz gerada e a matriz pequena

            pair = [(row, column), sim]                                            # Criacao de um par (POSICAO, GRAU DE SIMILARIDADE)
            pairs.append(pair)                                                     # Adicao do par a lista de pares

    highPair = getHighestSim(pairs)                                                # Obtem o par de maior grau de similaridade

    # ------------------------- IMPRESSAO -------------------------

    print('Posição: ({},{})'.format(highPair[0][0], highPair[0][1]))
    print('Similaridade máxima: {:.2f}%'.format(highPair[1]))




# Funcao de geracao de matrizes
def generateMatrix(dim):
    M = [[int(j) for j in input().split()] for i in range(dim)]
    return M




# Funcao de geracao de submatriz (recortar matriz)
def getSubmatrix(M, initRow, initCol, dim):
    subM = []                                                                      # Submatriz vazia

    for deltaRow in range(dim):
        newRow = []                                                                # Fileira vazia da submatriz
        for deltaCol in range(dim):
            newRow.append(M[initRow + deltaRow][initCol + deltaCol])               # Adicao dos elementos a fileira

        subM.append(newRow)                                                        # Adicao da fileira a submatriz

    return subM




# Funcao de calculo de grau de similaridade
def getSim(M1, M2):
    count = 0                                                                      # Contagem de elementos similares

    for row in range(len(M1)):                                                     # Laco para verificar cada fileira
        for column in range(len(M1)):                                              # Laco para verificar cada elemento da fileira atual
            if M1[row][column] == M2[row][column]:
                count += 1                                                         # Caso o elemento Mij da matriz 1 seja igual ao elemento Mij da matriz 2, entao eles sao similares e a contagem aumenta

    dim = len(M1)                                                                  # Dimensao de qualquer uma das duas matrizes (devem ser de dimensoes iguais)

    return count * 100 / (dim ** 2)                                                # Retorno do grau de similaridade




# Funcao de retorno de calculo de maior grau de similaridade
def getHighestSim(pairList):
  highestPair = pairList[0]                                                        # O maior par eh o primeiro (padrao)

  for pair in pairList:
    if pair[1] > highestPair[1]:                                                   # Caso um par P tenha maior similaridade que o maior par, entao o maior par se torna P
      highestPair = pair

  return highestPair                                                               # Retorno do maior par




main()
