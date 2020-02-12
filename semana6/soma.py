def soma_lista(lista):
    if len(lista) == 1:                #base da recusao
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])   #chamada recursiva

'''import pytest

@pytest.mark.parametrize('entrada, esperado', [
    ([1,1],2),
    ([1,2,3],6),
    ([2,2,2],6),
    ([3],3),
    ([2,2],4)
])

def testa_soma_lista(entrada, esperado):
    assert soma_lista(entrada) == esperado'''