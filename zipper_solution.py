"""A program that zips files inside a directory individually.

This program should not zip files that are already zipped!

Hint: Use os.walk to find files.
"""
import os
import zipfile
import time
from concurrent import futures


def files_to_zip(path):
    for dirpath, dirnames, filenames in os.walk(path):
        # Do not descend into subdirectories
        dirnames.clear()

        yield from (os.path.join(dirpath, filename)
                    for filename in filenames
                    if not filename.endswith('.zip'))


def zip_file(file_path):
    # Sleep here so we can detect speedup!
    time.sleep(0.1)

    with zipfile.ZipFile(file_path + '.zip', 'w') as zf:
        zf.write(file_path)


def main(path):
    """Main entry point.
    """
    print(f'Zipping files in {path}...')

    with futures.ProcessPoolExecutor() as pool:
        for f in files_to_zip(path):
            pool.submit(zip_file, f)


if __name__ == '__main__':
    import sys

    try:
        path = sys.argv[1]
    except IndexError:
        print(f'Usage: {sys.argv[0]} <directory>', file=sys.stderr)
        sys.exit(1)
    else:
        main(path)
