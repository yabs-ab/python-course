def runeberg_word_gen(path):
    """Generate words from the "Project Runeberg" text in `path`.
    """
    pass


def main(path):
    """Program entry point.
    """
    word_count = sum(1 for _ in runeberg_word_gen(path))
    print(f'Words in "{path}": {word_count}')


if __name__ == '__main__':
    import sys

    try:
        path = sys.argv[1]
    except IndexError:
        print(f'Usage: python {sys.argv[0]} <path>', file=sys.stderr)
        sys.exit(1)
    else:
        main(path)
