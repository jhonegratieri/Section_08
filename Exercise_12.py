

def sum_of_digits(number):
    numbers_digits = list(str(number))
    summation = 0

    for i in numbers_digits:
        summation += int(i)

    return summation


print(sum_of_digits(12457))
