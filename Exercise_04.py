from math import sqrt


def perfect_square(number):
    if number >= 1 and (sqrt(number) % 1) == 0:
        print(f'The number {number} is a perfect square.')
    else:
        print(f'The number {number} isn\'t a perfect square.')


perfect_square(16)
