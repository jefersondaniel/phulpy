import sys
import os
import argparse
from glob import glob
from datetime import datetime
from .phulpy import start
from .output import Output
from .version import version


def show_version():
    Output.out(Output.colorize(version, 'green'))


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument('tasks', nargs='*', default=['default'])
    parser.add_argument(
        '-v', '--version',
        action='store_true',
        help='Show phulpy version'
    )
    parser.add_argument(
        '--threads',
        default=1,
        type=int,
        help='Number of threads to start simultaneously'
    )
    args = parser.parse_args()

    if args.version:
        show_version()
        exit(0)

    files = glob('phulpyfile.py')
    try:
        if not len(files):
            raise Exception('There\'s no phulpyfile.py present.')
        path_backup = sys.path[:]
        sys.path.append(os.getcwd())
        __import__(files[0].split('.py')[0], globals(), locals(), [], 0)
        sys.path = path_backup
        start(args.tasks, args.threads)
    except Exception as e:
        error_message = str(e)

        Output.err(
            "[{}] {}".format(
                Output.colorize(
                    datetime.now().strftime('%H:%M:%S'),
                    'light_gray'
                ),
                Output.colorize(error_message, 'light_red')
            )
        )

        exit(1)


if __name__ == '__main__':
    __main__()
    exit(0)
