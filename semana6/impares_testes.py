import pytest


def encontra_impares2(lista):
    if len(lista) == 1:  # base da recusao
        if lista[0]//2 != 0:
            return lista[0]
        else:
            return []
    else:
        return [lista[0]] + encontra_impares(lista[1:])  # chamada recursiva


def encontra_impares(lista):
	if len(lista) == 0:
		return []
	if lista[0] % 2 != 0:
		return [lista[0]] + encontra_impares(lista[1:])
	return encontra_impares(lista[1:])


def encontra_impares3(lista):

    # Define a lista que armazenará os números ímpares:
    lis = []

    # Verifica se há elementos na lista:
    if len(lista) > 0:

        # Retira o primeiro elemento da lista:
        numero = lista.pop(0)

        # Verifica se o número é ímpar:
        if numero % 2 != 0:

            # Sim, então adiciona-o à lista de ímpares:
            lis.append(numero)

        # Faz a união do resultado atual com o retorno para o resto da lista:
        lis = lis + encontra_impares(lista)

    # Retorna a lista final:
    return lis


@pytest.mark.parametrize('entrada, esperado', [
    ([1, 1], [1, 1]),
    ([1, 2, 3], [1, 3]),
    ([2, 2, 2], []),
    ([3], [3]),
    ([2, 2], [])
])
def testa_encontra_impares(entrada, esperado):
    assert encontra_impares(entrada) == esperado


lista = [2, 3, 4, 5, 6, 7, 8, 9]
listanova = encontra_impares(lista)
print(listanova)
