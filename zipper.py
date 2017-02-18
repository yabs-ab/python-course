"""A program that zips files inside a directory individually.

This program should not zip files that are already zipped!

Hint: Use os.walk to find files.
"""


def main(path):
    """Main entry point.
    """
    print(f'Zipping files in {path}...')
    pass


if __name__ == '__main__':
    import sys

    try:
        path = sys.argv[1]
    except IndexError:
        print(f'Usage: {sys.argv[0]} <directory>', file=sys.stderr)
        sys.exit(1)
    else:
        main(path)
