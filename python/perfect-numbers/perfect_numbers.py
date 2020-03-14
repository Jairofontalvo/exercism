def classify(number):
    if number <= 0:
        raise ValueError("No es numero natural")

    res = 0
    for i in range(1, number):
        if number % i == 0:
            res += i

    if res > number:
        return 'abundant'
    elif res < number:
        return 'deficient'
    else:
        return 'perfect'
