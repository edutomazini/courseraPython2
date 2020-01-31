def soma_matrizes(m1, m2):
    linha1 = len(m1)
    coluna1 = len(m1[0])
    linha2 = len(m2)
    coluna2 = len(m2[0])

    if (linha1 != linha2): return False
    if (coluna1 != coluna2): return False

    matsoma = []
    for i in range(0,linha1):
        linha = []
        for j in range(0,coluna1):
            linha.append(m1[i][j] + m2[i][j])
        matsoma.append(linha)
    
    return matsoma