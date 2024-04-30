import pytest
from src import function_library


# Тест функции, которая проверяет, что значения во входном списке упорядочены от мин к макс
class TestBubbleSort:

    # Функция возвращает данные для проверки теста - отсортированный по возрастанию список
    @pytest.fixture
    def sorted_example(self):
        return [2, 3, 11, 14, 32]

    # Функция возвращает данные для выполнения теста - неотсортированный список
    @pytest.fixture
    def unsorted_example(self):
        return [11, 2, 32, 14, 3]

    # Функция возвращает данные для выполнения теста - неотсортированный список с одинаковыми значениями
    @pytest.fixture
    def unsorted_qeual_example(self):
        return [11, 2, 32, 14, 3, 11, 32]

    # Функция возвращает данные для проверки теста - отсортированный список с одинаковыми значениями
    @pytest.fixture
    def sorted_qeual_example(self):
        return [2, 3, 11, 11, 14, 32, 32]

    # Тест функции на несортированном списке, проверка значений с сортированным
    def test_on_ordered(self, sorted_example, unsorted_example):
        assert function_library.bubble_sort(unsorted_example) == sorted_example

    # Тест функции с одинаковыми значениями в списке
    def test_on_equal(self, sorted_qeual_example, unsorted_qeual_example):
        assert function_library.bubble_sort(unsorted_qeual_example) == sorted_qeual_example