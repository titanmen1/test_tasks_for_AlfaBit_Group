INDENT_TYPE = ' '
INDENT_SIZE = 4


def make_indent(depth: int, indent_size: int = INDENT_SIZE, indent_type: str = INDENT_TYPE) -> str:
    """
    Create indent.
    Args:
        depth: value for indent.
        indent_size: size of indent.
        indent_type: type of indent.
    Returns:
        indent
    """
    return indent_type * indent_size * depth


def render_humanized_dict(data: dict or str, depth: int = 0) -> str:
    """
    Render readable structure for human from python dict
    Args:
        data: data for render.
        depth: depth of render.
    Returns:
        rendered dict
    """
    # Формируем необходимый отступ в зависимости от текущей глубины
    indent = make_indent(depth)
    if isinstance(data, dict):
        # Берем ключ в словаре, чтобы его отобразить и чтобы взять дочерниее элементы
        key = list(data.keys())[0] if depth else "root"
        # С помощью рекурсии спускаемся по вложенным элементам до простых элементов
        rows = [render_humanized_dict(child, depth + 1) for child in data[key]["children"]]
        # Формируем строку со вложенными элементами
        return '{0}{1}\n{2}'.format(indent, key, ''.join(rows))
    # Формируем строку из простых элементов
    return f"{indent}{data}\n"


tariff_info = {
    "root": {
        "children": [
            {
                "Внутрисетевой роуминг": {
                    "children": [
                        {
                            "Internet": {
                                "children": [
                                    "Значение A"
                                ]
                            }
                        },
                        {
                            "MMS": {
                                "children": [
                                    "Входящие: 0.00",
                                    "Исходящие: 6.45",
                                    {
                                        "Междугородние": {
                                            "children": [
                                                "Входящие: 0.00",
                                                {
                                                    "Исходящие": {
                                                        "children": [
                                                            "Значение B"
                                                        ]
                                                    }
                                                }
                                            ]
                                        }
                                    },
                                    {
                                        "Местные": {
                                            "children": [
                                                "Входящие: 0.00",
                                            ]
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            },
            {
                "Домашняя сеть": {
                    "children": [
                        {
                            "Internet": {
                                "children": [
                                    "Значение C"
                                ]
                            }
                        }
                    ]
                }
            }
        ]
    }
}

print(render_humanized_dict(tariff_info))
