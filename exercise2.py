class KeyBasedDefaultDict:
    """A version of `collections.defaultdict` with key based factory.

    The factory function takes the key as a parameter, i.e.

    >>> d = KeyBasedDefaultDict({1: 1},
    ...                         default=lambda key: key - 1)
    >>> d[1], d[2]
    (1, 1)
    """
    pass


class AbstractShape:
    """An abstract geometrical shape.
    """
    # Implement an initializer that takes and sets a "name" attribute here!

    # Implement an abstract area() method here!
    pass


# Implement some shapes that inherit from AbstractShape!


if __name__ == '__main__':
    import doctest
    doctest.testmod()
