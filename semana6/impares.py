def encontra_impares(lista):
    if len(lista) == 0:
        return []

    if lista[0] % 2 != 0:
        return [lista[0]] + encontra_impares(lista[1:])
    else:
        return encontra_impares(lista[1:])

'''lista = [2, 3, 4, 5, 6, 7, 8, 9]
listanova = encontra_impares(lista)
print(listanova)'''