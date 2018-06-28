import sys
import os
import argparse
from glob import glob
from .phulpy import start


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument('tasks', nargs='*', default=['default'])
    args = parser.parse_args()
    files = glob('phulpyfile.py')
    try:
        if not len(files):
            raise Exception('There\'s no phulpyfile.py present.')
        path_backup = sys.path[:]
        sys.path.append(os.getcwd())
        __import__(files[0].split('.py')[0], globals(), locals(), [], 0)
        sys.path = path_backup
        start(args.tasks)
    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(str(e))
        exit(1)


if __name__ == '__main__':
    __main__()
