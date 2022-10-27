# Joao Pedro Cavalcante Albuquerque Costa
# 12121ECP021


# Funcao Principal
def main():
    # --------------------- Inicio do programa ---------------------


    meses = int(input())          # Numero de meses

    d1na = 0                      # No. de imunizados com a 1a dose e sem atraso para a 2a dose
    d1a = 0                       # No. de imunizados com a 1a dose e com atraso para a 2a dose
    d2na = 0                      # No. de imunizados com a 2a dose e sem atraso de aplicacao
    d2a = 0                       # No. de imunizados com a 2a dose e com atraso de aplicacao


    # -------------------------- Calculo ---------------------------


    d1na, d1a, d2na, d2a = whileMain(d1na, d1a, d2na, d2a, meses)       # Atribuicao dos resultados dos calculos


    # ------------------ Impressao dos resultados ------------------


    print('Pessoas completamente imunizadas:', d2na + d2a)              # D2 = D2NA (sem atraso) + D2A (com atraso)
    print('Pessoas imunizadas apenas com uma dose:', d1a + d1na)        # D1 = D1NA (sem atraso) + D1A (com atraso)
    print('Pessoas que tomaram a segunda dose com atraso:', d2a)
    print('Pessoas esperando a segunda dose com atraso:', d1a)




# Funcao de Calculo
def whileMain(D1NA, D1A, D2NA, D2A, months):
    while (months > 0):                             # Laco de calculos
        vac = int(input())                          # Numero de vacinas em um dado mes

        # PROCEDIMENTO 1: VACINAR D1A
        vac, D1A, D2A = distribute(vac, D1A, D2A)


        # PROCEDIMENTO 2: VACINAR D1NA
        if (vac >= D1NA):
            vac, D1NA, D2NA = distribute(vac, D1NA, D2NA)
        else:
            vac, D1NA, D2NA = distribute(vac, D1NA, D2NA)
            D1A += D1NA
            D1NA = 0


        # PROCEDIMENTO 3: VACINAR NOVAS PESSOAS
        D1NA += vac


        # FIM
        months -= 1;

    return D1NA, D1A, D2NA, D2A                     # Retorno dos dados sobre os imunizados




# Funcao de Distribuicao de Vacinas e Imunizados
def distribute(lote_vac, d_sub, d_add):
    n = min(lote_vac, d_sub)
    d_add += n                                      # O numero de imunizados com 2 doses aumenta conforme a quantidade de vacinados
    lote_vac -= n                                   # As vacinas usadas sao descontadas da contagem total
    d_sub -= n                                      # O numero de imunizados com apenas 1 dose diminui

    return lote_vac, d_sub, d_add                   # Retorno dos valores


main()
