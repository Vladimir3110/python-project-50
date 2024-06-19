<<<<<<< HEAD
from gendiff.scripts.gendiff import generate_diff
=======
import pytest
from gendiff import generate_diff
import yaml
>>>>>>> origin/main


with open('./tests/fixtures/expected_stylish.txt', 'r') as f:
    result_stylish = f.read().strip()
with open('./tests/fixtures/expected_plain.txt', 'r') as f:
    result_plain = f.read().strip()
with open('./tests/fixtures/expected_json.txt', 'r') as f:
    result_json = f.read().strip()
with open('./tests/fixtures/expected_nested_stylish.txt', 'r') as f:
    result_nested_stylish = f.read().strip()
with open('./tests/fixtures/expected_nested_plain.txt', 'r') as f:
    result_nested_plain = f.read().strip()
with open('./tests/fixtures/expected_nested_json.txt', 'r') as f:
    result_nested_json = f.read().strip()


def test_flat_files_stylish():
    assert result_stylish == \
           generate_diff('./tests/fixtures/test_before.json',
                         './tests/fixtures/test_after.json').strip()
    assert result_stylish == \
           generate_diff('./tests/fixtures/test_before.yml',
                         './tests/fixtures/test_after.yml').strip()


def test_nested_files_stylish():
    assert result_nested_stylish == \
           generate_diff('./tests/'
                         'fixtures/test_before_nested.json',
                         './tests/'
                         'fixtures/test_after_nested.json',
                         "stylish")
    assert result_nested_stylish == \
           generate_diff('./tests/'
                         'fixtures/test_before_nested.yaml',
                         './tests/'
                         'fixtures/test_after_nested.yml',
                         "stylish")


#
def test_flat_files_plain():
       expected_lines = [
           "Property 'proxy' was removed",
           "Property 'follow' was removed",
           "Property 'timeout' was updated. From 50 to 20",
           "Property 'verbose' was added with value: true",
       ]
       result_plain = generate_diff(
           './tests/fixtures/test_before.json',
           './tests/fixtures/test_after.json',
           "plain"
       )
       for line in expected_lines:
           assert line in result_plain


def test_nested_files_plain():
    assert result_nested_plain == \
           generate_diff('./tests/'
                         'fixtures/test_before_nested.json',
                         './tests/'
                         'fixtures/test_after_nested.json',
                         "plain").strip()
    assert result_nested_plain == \
           generate_diff('./tests/'
                         'fixtures/test_before_nested.yaml',
                         './tests/'
                         'fixtures/test_after_nested.yml',
                         "plain").strip()


def test_flat_files_json():
    assert result_json == \
           generate_diff('./tests/fixtures/'
                         'test_before.json',
                         './tests/fixtures/'
                         'test_after.json', "json").strip()
    assert result_json == \
           generate_diff('./tests/fixtures/'
                         'test_before.yml',
                         './tests/fixtures/'
                         'test_after.yml',
                         "json").strip()


def test_nested_files_json():
    assert result_nested_json == \
           generate_diff('./tests/fixtures/'
                         'test_before_nested.json',
                         './tests/fixtures/'
                         'test_after_nested.json',
                         "json").strip()
    assert result_nested_json == \
           generate_diff('./tests/fixtures/'
                         'test_before_nested.yaml',
                         './tests/fixtures/'
                         'test_after_nested.yml', "json").strip()
