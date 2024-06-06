import pytest
from gendiff import generate_diff


@pytest.fixture
def first_file_path(tmpdir):
    file_path = tmpdir.join("file1.json")
    file_path.write('{"host": "hexlet.io", "timeout": 50, "proxy": "123.234.53.22", "follow": false}')
    return str(file_path)


@pytest.fixture
def second_file_path(tmpdir):
    file_path = tmpdir.join("file2.json")
    file_path.write('{"timeout": 20, "verbose": true, "host": "hexlet.io"}')
    return str(file_path)


def test_generate_diff(first_file_path, second_file_path):
    expected_diff = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    assert generate_diff(first_file_path, second_file_path) == expected_diff
