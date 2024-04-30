from src import function_library
import pytest


# Тест функции, находящей простые числа, меньше заданного n
class TestCalculator:

    # Тестируем операцию сложения на коррктных данных. Функция возвращает списко элементов.
    def test_add_on_correct(self):
        assert function_library.calculator(51, 27, "+") == 78

    # Тестируем операцию вычитания на коррктных данных. Функция возвращает списко элементов.
    def test_subtract_on_correct(self):
        assert function_library.calculator(25, 11, "-") == 14

    # Тестируем операцию умножения на коррктных данных. Функция возвращает списко элементов.
    def test_multiply_on_correct(self):
        assert function_library.calculator(5, 6, "*") == 30

    # Тестируем операцию деления на коррктных данных. Функция возвращает списко элементов.
    def test_divide_on_correct(self):
        assert function_library.calculator(5, 1, "/") == 5

    # Тестируем программу на некоррктных данных. Функция вызывает исключение ZeroDivisionError.
    def test_dived_on_zero(self):
        # Когда мы подаем на вход программе число 0 - функция с оператором деления завершается с ошибкой
        # Данная строчка показывает, что внутри блока кода под ней должно возникнуть заданное исключение
        # и это нормальное поведение.
        with pytest.raises(ZeroDivisionError):
            function_library.calculator(5, 0, "/")