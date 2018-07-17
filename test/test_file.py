from phulpy.file import File


def TestFile(object):
    def test_init(self):
        relative_path = '/tmp/lala'
        file = File(relative_path)
        assert file.relative_path == relative_path
