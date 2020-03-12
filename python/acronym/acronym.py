def abbreviate(words):
    resultado = ''
    words = (
            (((words.upper()).replace('-', ' ')).
             replace('_', ' ')).replace(',', ' ')
            ).split()
    for letters in words:
        resultado += letters[0]
    return resultado
