import yaml
import json


def parse_file(filepath):
    with open(filepath, 'r') as f:
        if filepath.endswith(('.yaml', '.yml')):
            return yaml.safe_load(f)
        elif filepath.endswith('.json'):
            return json.load(f)
        else:
            raise ValueError(f"Неподдерживаемый формат файла: {filepath}")
