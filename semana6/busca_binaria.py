import pytest


def busca_binaria(lista, elemento, min=0, max=None):
    #print('-') #quantidade que aparece menos 1, eh a quantidade de recursao executada.
    if max == None:
        max = len(lista)-1

    if max < min:
        return False
    else:
        meio = min + (max-min)//2

    if lista[meio] > elemento:
        return busca_binaria(lista, elemento, min, meio-1)

    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio+1, max)

    else:
        return meio


a = [10, 20, 30, 40, 50, 60]
b = [-10, -2, 0, 5, 66, 77, 99, 102, 239, 567, 875, 934]

print(busca_binaria(b,99))


@pytest.mark.parametrize('lista, valor, esperado', [
    (a, 10, 0),
    (a, 20, 1),
    (a, 30, 2),
    (a, 40, 3),
    (a, 50, 4),
    (a, 60, 5),
    (a, 70, False),
    (a, 15, False),
    (a, -10, False),
])
def testa_busca_binaria(lista, valor, esperado):
    assert busca_binaria(lista, valor) == esperado
