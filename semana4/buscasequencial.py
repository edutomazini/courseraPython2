def busca_seq(lista, elemento):
    for i in range(len(lista)):
        print(i)
        if lista[i] == elemento:
            return i
    return False

def busca_binaria(lista, x):
    primeiro = 0
    ultimo = len(lista)-1
    while primeiro <= ultimo:
        meio = (primeiro+ultimo)//2
        if lista[meio]==x:
            return meio
        else:
            if x < lista[meio]:
                ultimo = meio -1
            else:
                primeiro = meio +1
    return -1

print(busca_seq(['a', 'e', 'i'], 'e'))
print(busca_seq([12, 13, 14], 15))

print(busca_binaria(['a', 'e', 'i'], 'e'))
print(busca_binaria([12, 13, 14,15], 15))