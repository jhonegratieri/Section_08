from math import sqrt


def hypotenuse(leg_a, leg_b):
    return sqrt(leg_a ** 2 + leg_b ** 2)


print(hypotenuse(30, 40))
