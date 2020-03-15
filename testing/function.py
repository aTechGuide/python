from typing import Union


def multiply(*args: Union[int, float]): # multiply(3, 5, 9)
    if len(args) ==0:
        raise ValueError("At least one value to miltiply must be passed")

    total = 1
    for arg in args:
        total *= arg

    return total
