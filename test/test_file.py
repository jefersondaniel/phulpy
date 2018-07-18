import sys
import pytest
from phulpy.file import File


@pytest.fixture
def open_mock(mocker):
    builtins = 'builtins' if sys.version_info >= (3,) else 'phulpy.file'
    mocker.patch(
        '{}.open'.format(builtins),
        mocker.mock_open(read_data='lala')
    )


@pytest.fixture
def file(mocker, open_mock):
    return File('/tmp/lala', read=False)


class TestFile(object):
    def test_init(self, open_mock):
        relative_path = '/tmp/lala'
        file = File(relative_path, read=True)
        assert file.relative_path == relative_path

    def test_getters_and_setters(self, file):
        assert '/tmp/lala' == str(file)

        assert 'lala' == file.content
        file.content = 'lele'
        assert 'lele' == file.content

        assert '/tmp/lala' == file.relative_path
        file.relative_path = '/tmp/lele'
        assert '/tmp/lele' == file.relative_path

        assert '/tmp/lala' == file.real_path
        file.real_path = '/tmp/lele'
        assert '/tmp/lele' == file.real_path

        assert 'lala' == file.name
        file.name = 'lele'
        assert 'lele' == file.name
