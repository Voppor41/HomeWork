import inspect
from pprint import pprint


def introspection_info(obj):

    info = {'type': type(obj),
                  'attributes': {},
                  'methods': [],
                  'module': obj.__module__ if hasattr(obj, '__module__') else "built-in"}

    for attr_name in dir(obj):
        # Избегаем внутренних атрибутов и методов, начинающихся с '__'
        if not attr_name.startswith('__'):
            attr_value = getattr(obj, attr_name)
            if callable(attr_value):
                # Добавляем метод в список методов
                info["methods"].append(attr_name)
            else:
                # Добавляем атрибут в словарь атрибутов
                info["attributes"][attr_name] = attr_value

    if callable(obj):
        info["signature"] = str(inspect.signature(obj))
        info["docstring"] = inspect.getdoc(obj)

    return info


number_info = introspection_info(42)
pprint(number_info)
