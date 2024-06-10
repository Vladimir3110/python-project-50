from gendiff.diff import find_diff, format_diff


def test_find_diff_empty():
    assert find_diff({}, {}) == {}


def test_find_diff_identical():
    data1 = {'a': 1, 'b': 2}
    data2 = {'a': 1, 'b': 2}
    assert find_diff(data1, data2) == {
        'a': ('unchanged', 1),
        'b': ('unchanged', 2)
    }


def test_find_diff_added():
    data1 = {'a': 1}
    data2 = {'a': 1, 'b': 2}
    assert find_diff(data1, data2) == {
        'a': ('unchanged', 1),
        'b': ('added', 2)
    }


def test_find_diff_deleted():
    data1 = {'a': 1, 'b': 2}
    data2 = {'a': 1}
    assert find_diff(data1, data2) == {
        'a': ('unchanged', 1),
        'b': ('deleted', 2)
    }


def test_find_diff_changed():
    data1 = {'a': 1, 'b': 2}
    data2 = {'a': 1, 'b': '2'}
    assert find_diff(data1, data2) == {
        'a': ('unchanged', 1),
        'b': ('changed', (2, '2'))
    }


def test_find_diff_complex():
    data1 = {'a': {'b': 1, 'c': 2}, 'd': 3}
    data2 = {'a': {'b': 1, 'd': 4}, 'e': 5}
    expected_diff = {
        'a': ('changed', ({'b': 1, 'c': 2}, {'b': 1, 'd': 4})),
        'd': ('deleted', 3),
        'e': ('added', 5),
    }
    assert find_diff(data1, data2) == expected_diff


def test_format_diff_empty():
    assert format_diff({}) == "{\n}"


def test_format_diff_added():
    diff = {'b': ('added', 2)}
    expected_output = "{\n  + b: 2\n}"
    assert format_diff(diff) == expected_output


def test_format_diff_deleted():
    diff = {'b': ('deleted', 2)}
    expected_output = "{\n  - b: 2\n}"
    assert format_diff(diff) == expected_output


def test_format_diff_changed():
    diff = {'a': ('changed', (1, '1'))}
    expected_output = "{\n  - a: 1\n  + a: 1\n}"
    assert format_diff(diff) == expected_output


def test_format_diff_unchanged():
    diff = {'a': ('unchanged', 1)}
    expected_output = "{\n    a: 1\n}"
    assert format_diff(diff) == expected_output


def test_format_diff_complex():
    diff = {
        'a': ('changed', ({'b': 1, 'c': 2}, {'b': 1, 'd': 4})),
        'd': ('deleted', 3),
        'e': ('added', 5),
    }
    expected_output = (
        "{\n"
        "  - a: {'b': 1, 'c': 2}\n"
        "  + a: {'b': 1, 'd': 4}\n"
        "  - d: 3\n"
        "  + e: 5\n"
        "}"
    )
    assert format_diff(diff) == expected_output
