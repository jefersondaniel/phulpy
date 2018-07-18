from phulpy.output import Output


class TestOutput(object):
    def test_out(self):
        Output.out('lala')

    def test_err(self):
        Output.err('lala')

    def test_colorize(self):
        assert 'lala' in Output.colorize('lala', 'red')
        assert 'lala' in Output.colorize('lala', 'unknown')
