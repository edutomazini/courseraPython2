def menor_nome(nomes):
    nomeret = nomes[0]
    for nome in nomes:
        if len(nome.strip().capitalize()) < len(nomeret):
            nomeret = nome.strip().capitalize()
    return nomeret.capitalize()
