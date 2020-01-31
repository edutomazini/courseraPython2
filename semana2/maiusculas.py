def maiusculas(frase):
    import re
    frase = re.sub(r'[,;:.!?0-9 ]+', '', frase)
    fraseMaiuscula = frase.upper()
    letrasRet = ''
    i = 0
    for letra in fraseMaiuscula:
        if letra == frase[i]:
            letrasRet += letra
        i+=1
    return letrasRet

print(maiusculas('oi, Daniela e David'))