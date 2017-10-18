import re
from itertools import islice


def ends_match(strings):
    """Count strings in `strings` where ends match.

    Counts the number of strings in `string` with length 2 or more
    where the first character is the same as the last.

    >>> ends_match(['this', 'is', 'a', 'test'])
    1
    """
    return sum(1 for s in strings
               if len(s) > 1 and s[0] == s[-1])


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
    return singular if n == 1 else plural or singular + 's'



def pig_latin(text):
    """Translate `text` to pig latin.

    Pig latin is constructed by moving the first letter of every word
    to the end and appending 'ay', i.e.

    >>> pig_latin('pigs go oink')
    'igspay ogay inkoay'
    """
    def translate(word):
        return word[1:] + word[0] + 'ay'

    return ' '.join(translate(word) for word in text.split())


def is_palindrome(text):
    """Check whether `text` is a palindrome.

    This function ignores whitespace and capitalization.

    >>> is_palindrome('Ni talar bra latin')
    True

    >>> is_palindrome('Rabarberbarbar')
    False
    """
    text = re.sub(r'\W+', '', text).casefold()

    middle = len(text) // 2
    return text[:middle] == text[:-middle - 1:-1]


def sorted_by_length_and_alphabetically(strings):
    """Return specially sorted copy of `strings`.

    The longest strings first and within a length alphabetically.

    >>> sorted_by_length_and_alphabetically(
    ...     ['this', 'is', 'a', 'weird', 'sort', 'order'])
    ['order', 'weird', 'sort', 'this', 'is', 'a']
    """
    def key(s):
        return (-len(s), s)

    return sorted(strings, key=key)


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
    def name_and_desc(line):
        return tuple(line.split('|')[:2])

    def is_comment(line):
        return line.startswith('#')

    return [name_and_desc(line) for line in lines
            if not is_comment(line)]


def strip_xml_tags(text):
    """Return a version of `text` stripped of xml tags.

    >>> strip_xml_tags('Vi kan <a href="python.org">Python</a>!')
    'Vi kan Python!'
    """
    return re.sub(r'<.*?>', '', text)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
