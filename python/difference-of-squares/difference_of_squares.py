def square_of_sum(number):
    sum = 0
    for c in range(1, number+1):
        sum += c
    return sum**2


def sum_of_squares(number):
    square = 0
    for c in range(1, number+1):
        square += c**2
    return square


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
