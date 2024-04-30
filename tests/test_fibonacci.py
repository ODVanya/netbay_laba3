from src import function_library


# Тест функции, находящей простые числа, меньше заданного n
class TestFibonacci:

    # Тестируем программу на корректных данных. Функция возвращает список элементов.
    def test_on_correct_n(self):
        assert function_library.fibonacci(7) == [1, 1, 2, 3, 5, 8, 13]

    # Тестируем программу на некоррктных данных. Функция возвращает пустой список [].
    def test_on_incorrect(self):
        # Когда мы подаем на вход программе число 0 или отрицательное - программа должна вернуть пустой список.
        assert function_library.fibonacci(0) == []