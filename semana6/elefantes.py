def incomodam(n):
    if type(n) != type(1):
        return ""
    if n <= 0:
        return ""
    else:
        '''if n == 1:
            return "incomodam "
        else:'''
        return "incomodam " + incomodam(n-1)


'''def elefantes(n):
    if type(n) != type(1):
        return ""
    if n < 0:
        return ""
    if n == 0:
        return ""
    else:
        if n == 1:
            return "Um elefante incomoda muita gente" + elefantes(n-1)
        else:
            return str(n) + " elefantes incomodam muito mais" + elefantes(n-1)'''

def elefantes2(n):
    if n < 2:
        return ''
    elif n == 2:
        return 'Um elefante incomoda muita gente\n' + str(n) + ' elefantes ' + incomodam(n) + 'muito mais\n'
    else:
        return elefantes2(n-1) + str(n-1) + ' elefantes incomodam muita gente\n' + str(n) + ' elefantes ' + incomodam(n) + 'muito mais\n'

def elefantes(n):
    if type(n) != type(1):
        return ""
    if n <= 0:
        return ""
    if n == 1:
        musica = "Um elefante incomoda muita gente\n"
        return musica
    else:
        musica = str(n) + " elefantes " + str(incomodam(n)) + "muito mais\n"
        musica = musica + str(n) + " elefantes incomodam muita gente\n"
        return elefantes(n-1) + musica

# print(incomodam(7))
print(elefantes(0))
print('')
print(elefantes2(0))
