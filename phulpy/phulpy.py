class Phulpy:
    __tasks__ = {}

    def task(self, fn):
        self.__tasks__[fn.__name__] = fn
        return fn

    def start(self, tasks):
        for task in tasks:
            if task in self.__tasks__:
                self.__tasks__[task](self)
            else:
                raise Exception('There is no task named {}'.format(task))


phulpy = Phulpy()


def task(fn):
    phulpy.task(fn)
    return fn


def start(tasks):
    phulpy.start(tasks)
