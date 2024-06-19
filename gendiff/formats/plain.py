"""
рефакторинг кода с учетом снижения цикломатической сложности
 и улучшения читаемости:
Функция `to_str` переписана:
   -  Используется `isinstance` для проверки типов
 данных, что делает код чище.
   - Условия с `True`, `False`, `None` сгруппированы для
 лучшей читаемости.
   -  Проверка на `0` и `"0"` объединена.
"""


def plain(dict_diff: dict):
    return form_string(add_path(dict_diff))


def add_path(tree):
    def walk_(nod, path, new_tree=[]):
        for child in nod:
            new_path = f"{path}{child['name']}."
            child.update({"path": path})
            new_tree.append(child)
            if "children" in child:
                walk_(child.get("children"), new_path)
        return new_tree
    return walk_(tree, "")


def form_string(nod):
    strings = []
    for child in nod:
        property = f"{child['path']}{child['name']}"
        status = child['status']
        if status != "nested" and status != "same":
            string = f"Property '{property}' was {status}"
            if status == "added":
                value = to_str(child["value"])
                string += f" with value: {value}"
            if status == "updated":
                old_value = to_str(child["old_value"])
                new_value = to_str(child["new_value"])
                string += f". From {old_value} to {new_value}"
            strings.append(string)
    return "\n".join(strings)


def to_str(value):
    if isinstance(value, dict):
        return "[complex value]"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    if isinstance(value, (int, float)) or value == "0":
        return str(value)
    return f"'{value}'"
