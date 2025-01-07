import sys
from pprint import pprint
import inspect

def introspection_info(obj):
    info = {}

    # Получаем тип объекта
    info['type'] = type(obj).__name__

    # Получаем список атрибутов объекта (не вызываемых и не начинающихся с "__")
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    info['attributes'] = attributes

    # Получаем список методов объекта (вызываемых и не начинающихся с "__")
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    info['methods'] = methods

    # Получаем модуль, к которому принадлежит объект
    info['module'] = obj.__module__ if hasattr(obj, '__module__') else 'N/A'

    # Проверяем, является ли объект классом и собираем дополнительную информацию
    if inspect.isclass(obj):
        info['is_class'] = True
        info['base_classes'] = [base.__name__ for base in inspect.getmro(obj)[1:]]
    # Проверяем, является ли объект функцией
    elif inspect.isfunction(obj):
        info['is_function'] = True
        info['signature'] = inspect.signature(obj)
    # Проверяем, является ли объект методом
    elif inspect.ismethod(obj):
        info['is_method'] = True
        info['signature'] = inspect.signature(obj)
    # Проверяем, является ли объект модулем
    elif inspect.ismodule(obj):
        info['is_module'] = True
        info['file'] = inspect.getfile(obj)
    # Проверяем, является ли объект встроенной функцией
    elif inspect.isbuiltin(obj):
        info['is_builtin'] = True

    return info

# Пример использования с числом
number_info = introspection_info(42)
print("Информация о числе 42:")
pprint(number_info)

# Определяем класс для демонстрации интроспекции
class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        pass

# Создаем объект класса и получаем информацию о нем
my_object = MyClass(10)
object_info = introspection_info(my_object)
print("\nИнформация о объекте MyClass:")
pprint(object_info)
