#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers or floats and returns an integer.

    Args:
        a (int or float): The first number to add.
        b (int or float, optional): The second number to add. Defaults to 98.

    Raises:
        TypeError: If a or b is not an integer or float.

    Returns:
        int: The sum of a and b, casted to an integer.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        if isinstance(a, (int, float)):
            raise TypeError("b must be an integer")
        else:
            raise TypeError("a must be an integer")

    a = int(a)
    b = int(b)

    return a + b
