# Algoritmo de verificacao de senhas sobre a serie infantil "Castelo Ra-Tim-Bum".
# O usuario informa uma senha composta por numeros separados por espacos.
# Em seguida, o programa verifica se eh possivel ordenar os valores permutando-os de maneira similar a uma rotacao.
# Por fim, informa-se se a senha atende a tal verificacao.


def main():
    # Variaveis iniciais
    senha = [int(i) for i in input().split()]   # Senha
    size = len(senha)                           # Tamanho da senha
    verify = False                              # Verificacao da validade da senha

    for i in range(size):                       # A senha eh rotacionada um numero de vezes igual ao seu tamanho, logo obtem-se todas as suas possiveis rotacoes
        senha = rotate(senha)                   # Rotaciona a lista

        for j in range(size - 1):               # Verifica se cada numero eh menor ou igual ao seu sucessor na lista --> Se a condicao for verdadeira para todos, a lista esta ordenada em ordem crescente
            if (senha[j] <= senha[j + 1]):
                verify = True                   # Sempre que o numero for menor ou igual ao seu sucessor, a verificacao eh valida
            else:
                verify = False                  # Caso haja um numero maior que seu sucessor, a lista nao esta ordenada, e portanto, a verificacao eh invalida e a checagem eh interrompida
                break

        if (verify):                            # Se houver um caso em que os numeros estao ordenados, nao eh necessario verificar as combinacoes restantes
            break
    
    # Impressao de mensagem de acordo com a senha
    if (verify):
        print('Klift, Kloft, Still, a porta se abriu')
    else:
        print('Senha incorreta')



# Funcao de rotacao
def rotate(pw):
    size = len(pw)                              # Tamanho da senha
    first = pw[0]                               # Captura o primeiro elemento da senha

    # Laco de rotacao
    for i in range(0, size - 1):
        pw[i] = pw[i + 1]                       # Cada elemento se torna o elemento sucessor (elemento posterior)

    pw[-1] = first                              # O ultimo elemento se torna o primeiro elemento

    return pw                                   # Retorna a senha rotacionada

main()
