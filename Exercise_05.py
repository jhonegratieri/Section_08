from math import pi


def sphere_volume(radius):
    print(f'The volume of a sphere of radius {radius} is {round((4 / 3) * pi * radius ** 3, 2)}.')


sphere_volume(10)
