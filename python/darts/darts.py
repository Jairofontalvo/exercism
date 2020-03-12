def score(x, y):
    r = pow(x, 2) + pow(y, 2)
    if r <= pow(1, 2):
        return 10
    elif r <= pow(5, 2):
        return 5
    elif r <= pow(10, 2):
        return 1
    else:
        return 0
