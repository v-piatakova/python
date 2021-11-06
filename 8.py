#! / usr / bin / python
# - * - coding: utf-8 - * -
import itertools

def get(array):
    if (len(array) < 2):
        print("None")
    else:
        a, b = itertools.tee(array)
        next(b, None)

        print(zip(a, b))


get([1, 4, 6, 5])
