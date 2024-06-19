from gendiff.parser import parse_file
import yaml


def test_parse_yaml_file(tmpdir):
    file_content = """
    key1: value1
    key2:
    - item1
    - item2
    """
    filepath = tmpdir.join("test.yaml")
    filepath.write(file_content)
    expected_data = {'key1': 'value1', 'key2': ['item1', 'item2']}
    assert parse_file(str(filepath)) == expected_data
