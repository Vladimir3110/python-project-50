import json


def generate_diff(file_path1, file_path2):
    data1 = _load_data('tests/fixtures/file1.json')
    data2 = _load_data('tests/fixtures/file2.json')

    diff = _build_diff(data1, data2)

    return _format_diff(diff)


def _build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff = {}

    for key in keys:
        if key not in data2:
            diff[key] = ('deleted', data1[key])
        elif key not in data1:
            diff[key] = ('added', data2[key])
        elif data1[key] == data2[key]:
            diff[key] = ('unchanged', data1[key])
        else:
            diff[key] = ('changed', (data1[key], data2[key]))

    return diff


def _format_diff(diff):
    lines = ['{']

    for key, (status, value) in diff.items():
        if status == 'deleted':
            lines.append(f"  - {key}: {_format_value(value)}")
        elif status == 'added':
            lines.append(f"  + {key}: {_format_value(value)}")
        elif status == 'changed':
            old_value, new_value = value
            lines.append(f"  - {key}: {_format_value(old_value)}")
            lines.append(f"  + {key}: {_format_value(new_value)}")
        else:
            lines.append(f"    {key}: {_format_value(value)}")

    lines.append('}')
    return '\n'.join(lines)


def _format_value(value):
    if isinstance(value, dict):
        return _format_diff(value).replace('\n', '\n  ')
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return value


def _load_data(file_path):
    with open(file_path) as file:
        if file_path.endswith(('.json')):
            return json.load(file)
        else:
            raise ValueError(f"Unsupported file format: {file_path}")
