import pytest

from z2 import merge_and_write

@pytest.fixture
def my_fixture():
    path1 = '1.txt'
    path2 = '2.txt'
    path3 = '3.txt'

    with open(path1, 'r') as f1:
        data1 = f1.read()
    with open(path2, 'r') as f2:
        data2 = f2.read()

    with open(path3, 'w') as f:
        f.write(data1 + data2)

    return data1 + data2

def test_merge_and_write(final):
    assert final == "data1 data2"

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        merge_and_write('who.txt', 'where.txt', 'when.txt')