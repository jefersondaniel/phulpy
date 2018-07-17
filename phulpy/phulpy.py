import os
from output import Output
from datetime import datetime
from time import time
from source import Source
from helpers import mkdir


class Phulpy:
    __tasks__ = {}

    def task(self, fn):
        self.__tasks__[fn.__name__] = fn
        return fn

    def src(self, glob_patterns, read=True):
        return Source(glob_patterns, read=read)

    def iterate(self, callback):
        def __pipe__(src):
            [callback(file) for file in src.files]

        return __pipe__

    def filter(self, callback):
        def __pipe__(src):
            src.files = [file for file in src.files if callback(file)]

        return __pipe__

    def dest(self, path):
        mkdir(path)

        def __pipe__(src):
            for file in src.files:
                dirname = os.path.join(
                    path,
                    os.path.dirname(file.relative_path)
                )
                basename = os.path.basename(file.relative_path)
                mkdir(dirname)
                file_final_path = os.path.join(dirname, basename)

                f = open(file_final_path, 'w')
                f.write(file.content)
                f.close()

        return __pipe__

    def clean(self):
        def __pipe__(src):
            for file in src.files:
                os.unlink(file.relative_path)

        return __pipe__

    def start(self, tasks):
        for task in tasks:
            if task in self.__tasks__:

                Output.out(
                    "[{}] Starting task {}".format(
                        Output.colorize(
                            datetime.now().strftime('%H:%M:%S'),
                            "light_gray"
                        ),
                        Output.colorize(task, "light_cyan")
                    )
                )

                start = time()
                self.__tasks__[task](self)

                Output.out(
                    "[{}] Starting task {} has finished in {} seconds".format(
                        Output.colorize(
                            datetime.now().strftime('%H:%M:%S'),
                            "light_gray"
                        ),
                        Output.colorize(task, "light_cyan"),
                        round(time() - start, 4)
                    )
                )
            else:
                raise Exception('There is no task named {}'.format(task))


phulpy = Phulpy()


def task(fn):
    phulpy.task(fn)
    return fn


def start(tasks):
    phulpy.start(tasks)
