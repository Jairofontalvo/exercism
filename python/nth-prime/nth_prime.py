def prime(number):
    if number <= 0:
        raise ValueError("Num negativo")

    primes, i = [2], 3
    while len(primes) < number:
        x = True
        for prime in primes:
            if i % prime == 0:
                x = False
                break
        if x:
            primes.append(i)
        i += 1

    return primes[-1]
