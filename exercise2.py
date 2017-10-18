class AbstractShape:
    """AbstractShape base class.

    Implement this class with an abstract property `area`

    >>> try:
    ...     AbstractShape().area
    ... except NotImplementedError:
    ...     print('Success!')
    Success!

    It should, of course, define `__repr__`

    >>> repr(AbstractShape())
    'AbstractShape()'
    """
    pass

class Rectangle(AbstractShape):
    """A rectangle.

    Define this subclass of `AbstractShape` that implements the `area`
    property.

    >>> Rectangle(4, 2).area
    8

    It should also define properties for `width` and `height`

    >>> r = Rectangle(48, 22)
    >>> r.width, r.height
    (48, 22)

    Also, make rectangles comparable with `==`

    >>> Rectangle(2, 4) == Rectangle(2, 4)
    True

    >>> Rectangle(2, 4) == Rectangle(2.1, 4)
    False

    And, its `__repr__` should `eval` to an equal object!

    >>> r = Rectangle(7, 21)
    >>> eval(repr(r)) == r
    True
    """
    pass

class KeyBasedDefaultDict(dict):
    """A version of `collections.defaultdict` with key based factory.

    The factory function takes the key as a parameter, i.e.

    >>> d = KeyBasedDefaultDict({1: 1},
    ...                         default=lambda key: key - 1)
    >>> d[1], d[2]
    (1, 1)
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
