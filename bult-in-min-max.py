# Module 3 Project, File 1 (Amber Speer)

"""Call the built-in maximum function for any three numbers"""
print(f'The maximum of 12, 27, and 36 is {max(12, 27, 36)}.')

"""Finds the minimum of any number of arguments"""
from math import e

def minimum(*args):
    """Returns the minimum of any number of arguments"""
    min_val=e
    for value in args:
        if min_val == e:
            min_val =value
        else:
            if value < min_val:
                min_val = value
    return min_val

print(f'The minimum of 15, 9, 27, and 14 is {minimum(15, 9, 27, 14)}.')


