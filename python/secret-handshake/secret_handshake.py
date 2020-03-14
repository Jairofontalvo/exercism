def commands(number):
    clave = {1: 'wink', 2: 'double blink', 4: 'close your eyes', 8: 'jump'}
    resul = [clave[i] for i in clave if i & number]
    if number & 16:
        return resul[::-1]
    else:
        return resul
