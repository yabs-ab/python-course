import re
import os
from itertools import chain
from itertools import tee
from collections import defaultdict
import random


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

    without_tags = (strip_xml_tags(line) for line in book_lines())

    book_words = chain.from_iterable(book_line.split()
                                     for book_line in without_tags)

    # Here we could add more steps to the pipeline, i.e.

    # casefolded = (word.casefold() for word in book_words)
    # without_punctuation = (word.strip('.,:;-*') for word in casefolded)
    # without_empty = (word for word in without_punctuation if word)

    yield from book_words


def word_count(path):
    """Count the words in the Project Runeberg book at `path`.
    """
    return sum(1 for _ in runeberg_word_gen(path))


def top_ten(path):
    """Top ten words used in `path`.
    """
    # There is a class in the standard library that does this:

    # from collections import Counter
    # return Counter(runeberg_word_gen(path)).most_common(10)

    words = defaultdict(int)

    for word in runeberg_word_gen(path):
        words[word] += 1

    return sorted(words.items(), key=lambda v: -v[1])[:10]


def pairwise(seq):
    a, b = tee(seq)
    next(b)
    return zip(a, b)


def random_walk(path, n):
    words = defaultdict(list)

    for word, after in pairwise(runeberg_word_gen(path)):
        words[word].append(after)

    res = [random.choice(list(words.keys()))]

    for _ in range(n):
        res.append(random.choice(words[res[-1]]))

    return res


def main(path):
    """Program entry point.
    """
    print(f'Words in "{path}": {word_count(path)}')

    for word, count in top_ten(path):
        print(word, '\t', count)

    print(' '.join(random_walk(path, 200)))


if __name__ == '__main__':
    import sys

    try:
        path = sys.argv[1]
    except IndexError:
        print(f'Usage: python {sys.argv[0]} <path>', file=sys.stderr)
        sys.exit(1)
    else:
        main(path)
