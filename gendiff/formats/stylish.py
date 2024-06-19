"""
Рефакторинг для уменьшения сложности:
1. Уменьшение сложности `make_string` (C901):
   - Вынесена логика форматирования отдельных узлов в
 отдельную функцию `_format_node`.
   - Это делает код `make_string` проще и улучшает его читаемость,
 так как он теперь фокусируется на общей структуре вывода.

2. Лишний пробел (W291):
   - Лишний пробел в конце строки 37 был удалён.

3. Неверный отступ (E128):
   - Отступ в строке 38 был исправлен для соответствия PEP 8
"""


from gendiff.comparison_tree import compare_dicts
from gendiff.constants import SPACES_PER_LEVEL, SHIFT_LEFT


def stylish(dict_diff: dict):
    return make_string(dict_diff)


def make_string(tree, depth=1):
    result = []
    for child in tree:
        result.append(_format_node(child, depth))
    return ("{\n" + "\n".join(result)
            + "\n" + SPACES_PER_LEVEL * (depth - 1) * " " + "}")


def _format_node(node, depth):
    """Форматирует строку для одного узла дерева."""
    indent = make_indent(depth)
    new_depth = depth + 1
    status = node['status']
    if status == 'removed':
        return (f"{indent}- {node['name']}: "
                f"{to_str(node['value'], new_depth)}")
    if status == 'added':
        return (f"{indent}+ {node['name']}: "
                f"{to_str(node['value'], new_depth)}")
    if status == 'nested':
        return (f"{indent}  {node['name']}: "
                f"{make_string(node['children'], new_depth)}")
    if status == 'updated':  # Условие перенесено на отдельный уровень
        return (f"{indent}- {node['name']}: "
                f"{to_str(node['old_value'], new_depth)}\n"
                f"{indent}+ {node['name']}: "
                f"{to_str(node['new_value'], new_depth)}")
    if status == 'same':
        return (f"{indent}  {node['name']}: "
                f"{to_str(node['value'], new_depth)}")
    return None  # Добавлено для полноты


def to_str(value, depth=0):
    """Преобразует значение в строку."""
    if isinstance(value, dict):
        return make_string(compare_dicts(value, value), depth)
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    if isinstance(value, (int, float)) or value == "0":
        return str(value)
    return value


def make_indent(depth):
    indent = (depth * SPACES_PER_LEVEL - SHIFT_LEFT) * " "
    return indent
