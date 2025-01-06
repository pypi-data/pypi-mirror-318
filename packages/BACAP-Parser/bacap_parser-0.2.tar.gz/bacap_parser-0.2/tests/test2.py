import timeit


# Класс с использованием __slots__
class SlotsClass:
    __slots__ = ('a', 'b', 'c')

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


# Класс без __slots__, использующий __dict__
class DictClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


# Функции для тестирования
def test_slots_access():
    obj = SlotsClass(1, 2, 3)
    return obj.a, obj.b, obj.c


def test_dict_access():
    obj = DictClass(1, 2, 3)
    return obj.a, obj.b, obj.c


# Настройка и выполнение тестов
slots_time = timeit.timeit('test_slots_access()', globals=globals(), number=1_000_0000)
dict_time = timeit.timeit('test_dict_access()', globals=globals(), number=1_000_0000)

# Результаты
print(f"Время доступа для класса с __slots__: {slots_time:.5f} секунд")
print(f"Время доступа для класса с __dict__: {dict_time:.5f} секунд")