class Ordenador:
    def selecao_direta(self, lista):
        fim = len(lista)
        for i in range(fim -1):
            posicao_do_minimo = i
            for j in range(i+1,fim):
                if lista[j]<lista[posicao_do_minimo]:
                    posicao_do_minimo = j
            lista[i],lista[posicao_do_minimo]=lista[posicao_do_minimo], lista[i]

    def bolha(self, lista):
        fim = len(lista)
        for i in range(fim-1, 0, -1):
            for j in range(i):
                if lista[j]>lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

def selecao_direta2(lista):
    fim = len(lista)
    for i in range(fim-1):
        pos_menor = i
        for j in range(i+1,fim):
            if lista[j] < lista[pos_menor]:
                pos_menor = j
        lista[i],lista[pos_menor] = lista[pos_menor],lista[i]
    return lista

numeros = [55, 33, 0, 900, -432, 10, 77, 2, 11]
numeros = [-432, 0, 2, 10, 11, 33, 55, 77, 900]

o = Ordenador()
lista = [2,23,234,21,6,9,12,21,3,5,9,0]
#o.selecao_direta(lista)
o.bolha(lista)
print(lista)
selecao_direta2(numeros)
print(numeros)