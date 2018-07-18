import pytest
import errno
from mock import Mock
from phulpy.helpers import mkdir


class TestHelpers(object):
    def test_mkdir_success(self, mocker):
        error = OSError()
        error.errno = errno.EEXIST
        mocker.patch('os.makedirs', Mock(side_effect=error))
        mocker.patch('os.path.isdir', Mock(return_value=True))
        mkdir('/tmp/lala')

        error.errno = 1
        with pytest.raises(OSError):
            mkdir('/tmp/lala')
