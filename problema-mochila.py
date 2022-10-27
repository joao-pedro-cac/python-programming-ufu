# Joao Pedro Cavalcante Albuquerque Costa
# 12121ECP021


# Funcao Principal
def main():

    # -------------------- VARIAVEIS --------------------


    bagWeight = 0;                                                # Peso total da mochila
    bagValue = 0;                                                 # Valor total da mochila

    num = int(input())                                            # Numero de objetos
    capacity = int(input())                                       # Capacidade da mochila

    weights = [int(input()) for i in range(num)]                  # Lista de pesos
    values = [int(input()) for i in range(num)]                   # Lista de valores
    ratios = [values[i] / weights[i] for i in range(num)]         # Lista de razoes (valor / peso)

    menor_peso = minimo(weights)                                  # Peso do objeto mais leve


    # --------------------- CALCULO ---------------------


    while (capacity >= menor_peso and len(ratios) > 0):           # Enquanto a capacidade
        maior_razao = maximo(ratios)                              # Elemento de maior razao
        index = getIndex(ratios, maior_razao)                     # Indice do elemento de maior razao
        maior_peso = weights[index]                               # Peso do elemento de maior razao
        maior_valor = values[index]                               # Valor do elemento de maior razao

        # Ocorre caso o objeto caiba na mochila (caso nao caiba, o objeto eh meramente descartado)
        if (maior_peso <= capacity):
            bagValue += maior_valor                               # A mochila se torna mais valiosa
            bagWeight += maior_peso                               # A mochila se torna mais pesada
            capacity -= maior_peso                                # A capacidade atual diminui

        # Deleta os dados do elemento selecionado
        del weights[index]
        del values[index]
        del ratios[index]


    # --------------- IMPRESSAO DOS DADOS  --------------


    print(bagValue)
    print(bagWeight)



# Funcao que retorna o maior valor de uma lista
def maximo(lista):
    maxVal = lista[0]

    for i in lista:
        if i > maxVal:
            maxVal = i

    return maxVal


# Funcao que retorna o menor valor de uma lista
def minimo(lista):
    minVal = lista[0]

    for i in lista:
        if i < minVal:
            minVal = i

    return minVal


# Funcao que obtem o primeiro indice de um dado elemento (caso nao haja objeto na lista, a funcao retorna -1)
def getIndex(lista, elemento):
    index = -1

    for i in range(len(lista)):
        if lista[i] == elemento:
            index = i
            break

    return index



# Chamada da funcao principal
main()
