from .output import Output
from datetime import datetime
from time import time


class Phulpy:
    __tasks__ = {}

    def task(self, fn):
        self.__tasks__[fn.__name__] = fn
        return fn

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
