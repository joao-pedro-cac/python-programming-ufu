# Algoritmo de verificacao de paridade em DNA.
# O usuario informa uma fita de DNA e uma fita primer, ambas como sequencias de letras representando bases nitrogenadas.
# O computador entao informa os locais em que eh possivel parear ambas as fitas segundo a complementaridade das bases.


# Funcao principal
def main():
    # -------------------VARIAVEIS --------------------
    dna = input()
    dna = dna[1:len(dna) - 1]                       # Retira '5' e '3' da fita de DNA

    primer = input()
    primer = primer[1:len(primer) - 1][::-1]        # Retira '5' e '3' do primer e inverte-o


    positions = []                                  # Lista de posicoes na sequencia de DNA


    # ------------------- CALCULO --------------------


    # Os lacos aninhados verificam em conjunto se as 'n' proximas bases do DNA sao complementares as 'n' bases do primer
    for i in range(len(dna) - len(primer) + 1):
        signal = False                              # Variavel de sinalizacao

        for j in range(len(primer)):                # Laco de verificacao de complementaridade (verifica se as proximas 'n' bases do DNA sao complementares ao primer)
            pair = [dna[i + j], primer[j]]          # Lista de par DNA - primer

            if checkComp(pair):
                signal = True                       # Caso uma base do DNA seja complementar a base correspondente do primer, a sinalizacao eh verdadeira
            else:
                signal = False                      # No momento em que uma base do DNA nao eh complementar a base do primer, a sinalizacao se torna falsa para todo o trecho do DNA e a verificacao se encerra
                break

        if signal:                                  # A sinalizacao se torna verdadeira se todas as 'n' proximas bases do DNA forem complementares ao primer, e com isso, coloca-se a posicao do trecho do DNA na lista de posicoes
            positions.append(i + 1)                 # A posicao do trecho de DNA complementar ao primer eh adicionada a lista de posicoes



    # ------------------- RESULTADOS FINAIS --------------------

    showPositions(positions)                        # As posicoes dos trechos de DNA complementares ao primer sao impressas





# Funcao de impressao de posicoes
def showPositions(posList):
    if len(posList) > 0:                            # Caso haja ao menos uma posicao correspondente no DNA, elas sao impressas
        for i in posList:
            print('Ligacao na posicao', i)
    else:
        print('Nenhuma ligacao')                    # Caso nao haja posicoes correspondentes, informa-se que nao ha ligacoes





# Funcao de checagem de complementaridade (verdadeiro para bases complementares, falso para bases nao complementares)
def checkComp(pair):                                # Recebe um par DNA - primer
    dnaC = pair[0]                                  # Componente (base) do DNA a ser analisado
    primerC = pair[1]                               # Componente (base) do primer a ser analisado

    if (dnaC == 'A' and primerC == 'T'):            # A <-> T
        return True
    elif (dnaC == 'T' and primerC == 'A'):          # T <-> A
	    return True
    elif (dnaC == 'C' and primerC == 'G'):          # C <-> G
	    return True
    elif (dnaC == 'G' and primerC == 'C'):          # G <-> C
	    return True
    else:                                           # Nao ha complementaridade
	    return False




main()
