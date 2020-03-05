def is_armstrong_number(number):
    cadena = str(number)
    length = len(cadena)
    x = 0
    for i in cadena:
        x = x + int(i)**length
    if x == number:
        return True
    else:
        return False
