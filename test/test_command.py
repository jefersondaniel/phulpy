from phulpy.command import Command


class TestCommand(object):
    def test_constructor(self):
        Command('ls', None, None, None, False, None, None, None)

    def test_start(self):
        c = Command('ls', None, None, None, True, lambda e: e, lambda e: e, lambda e, x, y: e)
        c.start()

        c = Command('ping -d', None, None, None, True, lambda e: e, lambda e: e, lambda e, x, y: e)
        c.start()
