from math import pi


def cylinder_volume(height, radius):
    return round(pi * height * radius ** 2, 2)


print(cylinder_volume(10, 10))
