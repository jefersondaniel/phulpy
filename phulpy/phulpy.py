
__tasks__ = {}


def task(fn):
    __tasks__[fn.__name__] = fn
    return fn


def run_tasks(tasks):
    for task in tasks:
        if task in __tasks__:
            __tasks__[task]()
        else:
            raise Exception('There is no task named {}'.format(task))
