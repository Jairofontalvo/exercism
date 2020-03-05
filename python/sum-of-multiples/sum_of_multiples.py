def sum_of_multiples(limit, multiples):
    result = []
    for i in range(1, limit):
        for j in multiples:
            if j != 0 and i % j == 0:
              result.append(i)
              break
    return sum(result)
