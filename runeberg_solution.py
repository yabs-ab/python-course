import re
import os
from itertools import chain
from collections import Counter

def strip_xml_tags(text):
    return re.sub(r'<.*?>', '', text)


def runeberg_word_gen(path):
    """Generate words from the "Project Runeberg" text in `path`.
    """
    def articles_lines():
        with open(os.path.join(path, 'Articles.lst'), 'r') as f:
            yield from f

    basenames = (line.split('|')[0]
                 for line in articles_lines()
                 if not line.startswith('#'))

    chapter_paths = (os.path.join(path, basename + '.html')
                     for basename in basenames)

    def book_lines():
        for chapter_path in chapter_paths:
            with open(chapter_path, 'r') as f:
                yield from f

    book_words = chain.from_iterable(book_line.split()
                                     for book_line in book_lines())

    yield from (strip_xml_tags(word) for word in book_words)


def word_count(path):
    """Count the words in the Project Runeberg book at `path`.
    """
    return sum(1 for _ in runeberg_word_gen(path))


def top_ten(path):
    """Top ten words used in `path`.
    """
    counter = Counter(runeberg_word_gen(path))
    return counter.most_common(10)


def main(path):
    """Program entry point.
    """
    print(f'Words in "{path}": {word_count(path)}')

    for word, count in top_ten(path):
        print(word, '\t', count)

if __name__ == '__main__':
    import sys

    try:
        path = sys.argv[1]
    except IndexError:
        print(f'Usage: python {sys.argv[0]} <path>', file=sys.stderr)
        sys.exit(1)
    else:
        main(path)
