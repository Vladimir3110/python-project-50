def compare_dicts(dict1, dict2):
    keys = list(set(dict1.keys()) | set(dict2.keys()))
    keys.sort()
    return [compare_keys(key, dict1, dict2) for key in keys]


def compare_keys(key, dict1, dict2):
    old_value = dict1.get(key)
    new_value = dict2.get(key)

    if key in dict1 and key not in dict2:
        return {
            "name": key,
            'value': old_value,
            'status': 'removed'
        }

    elif key not in dict1 and key in dict2:
        return {
            "name": key,
            'value': new_value,
            'status': 'added'
        }

    elif isinstance(old_value, dict) and isinstance(new_value, dict):
        return {
            "name": key,
            'children': compare_dicts(old_value, new_value),
            'status': 'nested'
        }

    elif old_value != new_value:
        return {
            "name": key,
            'old_value': old_value,
            'new_value': new_value,
            'status': 'updated'
        }

    elif old_value == new_value:
        return {
            "name": key,
            'value': old_value,
            'status': 'same'
        }
