from gendiff.formats.plain import plain
from gendiff.formats.stylish import stylish
from gendiff.formats.json import to_json


def select_formatter(dict, format_name):
    if format_name == "stylish":
        return stylish(dict)
    if format_name == "plain":
        return plain(dict)
    if format_name == "json":
        return to_json(dict)
