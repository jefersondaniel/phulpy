import sys
import pytest
from mock import Mock
from phulpy.phulpy import phulpy, task, start, TaskNotFound


@pytest.fixture(autouse=True)
def default_fixture(mocker):
    builtins = 'builtins' if sys.version_info >= (3,) else 'phulpy.phulpy'
    mocker.patch(
        '{}.open'.format(builtins),
        mocker.mock_open(read_data='lala')
    )
    mocker.patch('glob.glob', Mock(return_value=['/a/a', '/a/b']))
    mocker.patch('os.walk', Mock(return_value=[('/a/a', ['b'], ['a'])]))
    mocker.patch('os.unlink', Mock())
    mocker.patch('os.makedirs', Mock())
    mocker.patch('os.path.isfile', Mock(return_value=True))
    mocker.patch('os.path.dirname', Mock(return_value='b'))
    mocker.patch('os.path.basename', Mock(return_value='b'))


class TestPhulp(object):
    def test_task(self):
        @task
        def lala():
            pass
        assert 'lala' in phulpy.tasks

    def test_src(self, mocker):
        source_mock = Mock()
        mocker.patch('phulpy.source.Source', source_mock)
        source = phulpy.src(['lala'])
        assert source is not None

    def test_iterate(self):
        src = Mock()
        src.files = ['a', 'b']
        callback = Mock()
        iterator = phulpy.iterate(callback)
        iterator(src)
        assert callback.called

    def test_filter(self):
        src = Mock()
        src.files = ['a', 'b']
        callback = Mock()
        callback.side_effect = [True, False]
        iterator = phulpy.filter(callback)
        iterator(src)
        assert ['a'] == src.files

    def test_dest(self):
        src = Mock()
        src.files = [Mock()]
        iterator = phulpy.dest('lala')
        iterator(src)

    def test_clean(self):
        src = Mock()
        src.files = [Mock()]
        iterator = phulpy.clean()
        iterator(src)

    def test_execute(self):
        phulpy.execute('/bin/ls ""', quiet=True)

    def test_start(self):
        @task
        def with_argument(phulpy):
            pass

        @task
        def without_argument():
            pass

        start(['with_argument', 'without_argument'])

        with pytest.raises(TaskNotFound):
            start(['undefined'])
