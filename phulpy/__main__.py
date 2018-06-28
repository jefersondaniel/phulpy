import argparse
from glob import glob
from phulpy import run_tasks


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument('tasks', nargs='*', default=['default'])
    args = parser.parse_args()
    files = glob('phulpyfile.py')
    try:
        if not len(files):
            raise Exception('There\'s no phulpyfile.py present.')
        exec(open(files[0], 'r').read())
        run_tasks(args.tasks)
    except Exception as exception:
        print(exception.message)
        exit(1)


if __name__ == '__main__':
    __main__()
