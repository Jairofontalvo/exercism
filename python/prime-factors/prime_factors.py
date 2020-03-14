def factors(value):
    resul = []
    divisor = 2
    while value > 1:
        if value % divisor:
            divisor += 1
        else:
            resul.append(divisor)
            value = value / divisor
    return resul
