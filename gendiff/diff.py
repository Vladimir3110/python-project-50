def find_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff = {}
    for key in keys:
        if key not in data1:
            diff[key] = ('added', data2[key])
        elif key not in data2:
            diff[key] = ('deleted', data1[key])
        elif data1[key] == data2[key]:
            diff[key] = ('unchanged', data1[key])
        else:
            diff[key] = ('changed', (data1[key], data2[key]))
    return diff


def format_diff(diff):
    lines = ['{']
    for key, (status, value) in diff.items():
        if status == 'deleted':
            lines.append(f'  - {key}: {value}')
        elif status == 'added':
            lines.append(f'  + {key}: {value}')
        elif status == 'changed':
            lines.append(f'  - {key}: {value[0]}')
            lines.append(f'  + {key}: {value[1]}')
        else:
            lines.append(f'    {key}: {value}')
    lines.append('}')
    return '\n'.join(lines)
