# Joao Pedro Cavalcante Albuquerque Costa
# 12121ECP021

# Funcao principal
def main():
    tabuleiro = [input().split() for i in range(10)]                               # Matriz tabuleiro

    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'                                           # Alfabeto
    rows = chars[:10]                                                              # Fileiras (A - J)

    p = int(input())                                                               # No. de palpites

    # Laco de palpites
    for i in range(p):
        guess = input().split()                                                    # Palpite

        row = get_index(chars, guess[0]) + 1                                       # Fileira do palpite + conversao para numero (ex: E = fileira #5)
        col = int(guess[1])                                                        # Coluna do palpite

        tabuleiro = check_hit(tabuleiro, (row, col), chars)                        # Checagem de acerto




# Funcao de obtencao de indice de um elemento em uma lista
def get_index(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i                                                               # Se houver o elemento desejado na lista, retorna o indice de sua primeira ocorrencia

    return None                                                                    # Se nao houver o elemento desejado na lista, retorna nada




# Funcao de verificacao de pertencimento de um elemento a uma lista
def is_contained(lista, elem):
    for el in lista:
        if el == elem:
            return True                                                            # Se o elemento desejado estiver contido na lista, retorna Verdadeiro
    return False                                                                   # Se nao estiver contido, retorna Falso




# Funcao de contagem de ocorrencia de um elemento no tabuleiro
def count_item(table, elem):
    count = 0                                                                      # Variavel de contagem

    for row in table:                                                              # Percorre as fileiras
        for col in row:                                                            # Percorre as colunas
            if col == elem:
                count += 1                                                         # Se a casa do tabuleiro corresponder ao elemento desejado, a contagem aumenta

    return count
    



# Funcao de checagem de acerto
def check_hit(table, coords, chars):
    x, y = coords[0], coords[1]                                                    # Coordenadas x (fileira) e y (coluna)
    target = table[x - 1][y - 1]                                                   # Casa do palpite

    if is_contained(chars, target.upper()):                                        # Confere se a casa eh um navio
        table[x - 1][y - 1] = target.lower()                                       # Marca o navio atingido tornando a letra da casa minuscula

        if count_item(table, target.upper()) >= 1:
            print('atingiu o navio', target.upper())                               # Se houver uma casa de um dado navio intacta, a mensagem eh 'atingiu'
        else:
            print('afundou o navio', target.upper())                               # Se todas as casas de um dado navio forem atingidas, a mensagem eh 'afundou'
    else:
        print('agua')                                                              # Se a casa nao eh um navio, a mensagem eh 'agua'

    return table                                                                   # Retorna a tabela para salvar alteracoes


if __name__ == '__main__':                                                         # A funcao principal eh chamada apenas se o programa for executado como um script
    main()
