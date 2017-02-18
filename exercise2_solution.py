class KeyBasedDefaultDict(dict):
    """A version of `collections.defaultdict` with key based factory.

    The factory function takes the key as a parameter, i.e.

    >>> d = KeyBasedDefaultDict({1: 1},
    ...                         default=lambda key: key - 1)
    >>> d[1], d[2]
    (1, 1)
    """
    def __init__(self, *args, default=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._factory = default

    def __missing__(self, key):
        if self._factory:
            return self._factory(key)

        raise KeyError(key)


class AbstractShape:
    """An abstract geometrical shape.
    """
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError('area not implemented')


class Rectangle(AbstractShape):
    def __init__(self, width, height):
        super().__init__('rectangle')
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
