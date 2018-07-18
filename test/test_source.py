import sys
import pytest
from mock import Mock
from phulpy.source import Source


@pytest.fixture(autouse=True)
def default_fixture(mocker):
    builtins = 'builtins' if sys.version_info >= (3,) else 'phulpy.source'
    mocker.patch(
        '{}.open'.format(builtins),
        mocker.mock_open(read_data='lala')
    )
    mocker.patch('glob.glob', Mock(return_value=['/a/a', '/a/b']))
    mocker.patch('os.walk', Mock(return_value=[('/a/a', ['b'], ['a'])]))
    mocker.patch('os.path.isfile', Mock(return_value=True))


class TestSource(object):
    def test_pipe(self):
        source = Source(['/tmp/lala', '/tmp/**/*'], read=False)
        callback = Mock()
        source.pipe(callback)
        assert callback.called

    def test_getters(self):
        source = Source(['/tmp/lala', '/tmp/**/*'], read=False)
        assert 0 < len(source.files)

    def test_setters(self):
        source = Source(['/tmp/lala', '/tmp/**/*'], read=False)
        source.files = []
        assert 0 == len(source.files)
