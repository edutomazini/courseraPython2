def selecao_direta(lista):
    fim = len(lista)
    for i in range(fim-1):
        pos_menor = i
        for j in range(i+1,fim):
            if lista[j] < lista[pos_menor]:
                pos_menor = j
        lista[i],lista[pos_menor] = lista[pos_menor],lista[i]
    return lista

def ordenada(lista):
    listatemporaria = lista.copy()
    selecao_direta(lista)
    if lista == listatemporaria:
        return True
    else:
        return False

lista = [-432, 0, 2, 10, 11, 33, 55, 77, 900]

print(ordenada(lista))