def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def dimensoes(minha_matriz):
    print(str(len(minha_matriz))+'X'+str(len(minha_matriz[0])))

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


linha = int(input('digite a qtd de linha: '))
coluna = int(input('digite a qtd de colunas: '))

matriz1 = cria_matriz(linha,coluna)

linha2 = int(input('digite a qtd de linha: '))
coluna2 = int(input('digite a qtd de colunas: '))
matriz2 = cria_matriz(linha2, coluna2)
#print(matriz1)
#print(matriz2)
#dimensoes = dimensoes(matriz)
soma = soma_matrizes(matriz1, matriz2)
print(soma)
#print(dimensoes)
#minha_matriz = [[1], [2], [3]]
#dimensoes(minha_matriz)