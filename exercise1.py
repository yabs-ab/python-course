"""Some basic exercises!
"""


def ends_match(strings):
    """Count strings in `strings` where ends match.

    Counts the number of strings in `string` with length 2 or more
    where the first character is the same as the last.

    >>> ends_match(['this', 'is', 'a', 'test'])
    1
    """
    pass


def pluralize(n, singular, plural=None):
    """Pluralize `singular`.

    Uses `plural` if provided, otherwise appends 's' to `singular`.

    >>> pluralize(1, 'apple')
    'apple'

    >>> pluralize(2, 'apple')
    'apples'

    >>> pluralize(4, 'goose', 'geese')
    'geese'
    """
    pass


def pig_latin(text):
    """Translate `text` to pig latin.

    Pig latin is constructed by moving the first letter of every word
    to the end and appending 'ay', i.e.

    >>> pig_latin('pigs go oink')
    'igspay ogay inkoay'
    """
    pass


def is_palindrome(text):
    """Check whether `text` is a palindrome.

    This function ignores whitespace and capitalization.

    >>> is_palindrome('Ni talar bra latin')
    True

    >>> is_palindrome('Rabarberbarbar')
    False
    """
    pass


def sorted_by_length_and_alphabetically(strings):
    """Return specially sorted copy of `strings`.

    The longest strings first and within a length alphabetically.

    >>> sorted_by_length_and_alphabetically(
    ...     ['this', 'is', 'a', 'weird', 'sort', 'order'])
    ['order', 'weird', 'sort', 'this', 'is', 'a']
    """
    pass


def parse_index_lines(lines):
    """Parse sequence of `lines` of a hypothetical index file.

    Each line follows the format

        <name>|<description>|

    and this function returns a list of (name, description)
    tuples. Lines that start with a '#' are comments and should be
    ignored.

    >>> parse_index_lines(
    ...    ['# This is a comment and should be ignored!',
    ...     'name 1|description 1|',
    ...     'name 2|description 2|'])
    [('name 1', 'description 1'), ('name 2', 'description 2')]
    """
    pass


def strip_xml_tags(text):
    """Return a version of `text` stripped of xml tags.

    >>> strip_xml_tags('Vi är <a href="sylog.se">Sylog</a>!')
    'Vi är Sylog!'
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
