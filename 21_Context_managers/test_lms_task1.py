import pytest
from lms_task1 import OpenFile


@pytest.fixture
def openfile_to_test():
    with OpenFile('Hello', 'r+') as inF:
        yield inF

def test_fails():
    with pytest.raises(Exception):
        raise AttributeError

def test_if_exists(openfile_to_test):
    assert openfile_to_test.read() is not None


def test_is_written(openfile_to_test):
    openfile_to_test.write('My name is Kichy')
    openfile_to_test.seek(0)
    assert 'My name is Kichy' in openfile_to_test.read()
