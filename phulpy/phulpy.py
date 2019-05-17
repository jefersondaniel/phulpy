import os
from datetime import datetime
from time import time
from multiprocessing.dummy import Pool as ThreadPool
from .output import Output
from .source import Source
from .helpers import mkdir
from .command import Command


class TaskNotFound(Exception):
    pass


class Phulpy(object):
    __tasks = {}

    def task(self, fn):
        self.__tasks[fn.__name__] = fn
        return fn

    @property
    def tasks(self):
        return self.__tasks

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
            if task in self.__tasks:

                Output.out(
                    "[{}] Starting task {}".format(
                        Output.colorize(
                            datetime.now().strftime('%H:%M:%S'),
                            "light_gray"
                        ),
                        Output.colorize(task, "light_cyan")
                    )
                )

                task_fn = self.__tasks[task]
                start = time()

                if task_fn.__code__.co_argcount:
                    task_fn(self)
                else:
                    task_fn()

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
                raise TaskNotFound('There is no task named {}'.format(task))

    def execute(self, command, cwd=None, env=None, quiet=False, sync=True, on_stdout=None, on_stderr=None, on_finish=None):
        command = Command(
            command,
            cwd,
            env,
            quiet,
            sync,
            on_stdout,
            on_stderr,
            on_finish
        )
        command.start()

        return command


phulpy = Phulpy()


def task(fn):
    phulpy.task(fn)
    return fn


def start(tasks, threads=1):
    pool = ThreadPool(threads)
    pool.map(lambda task: phulpy.start([task]), tasks)
