# Функция определения n чисел Фибоначчи
# Принимает n
# Возвращает список чисел Фибоначчи
# Пример: 10 -> 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
def fibonacci(n):
    fib1 = fib2 = 1
    fib_list = []
    while n > 0:
        fib_list.append(fib1)
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    return fib_list


# Функция алгоритма сортировки пузырьком
# Пример:
# [11, 2, 32, 14, 3] -> [2, 3, 11, 14, 32]
def bubble_sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# Функция калькулятора принимает 3 аргумента: число 1, число 2 и знак
# действия: +, -, *, / выполняет действие и возвращает результат
# Пример:
# 8/4 -> 2
# 19-10 -> 9
# 5*6 -> 30
# 2+15 -> 17
def calculator(a, b, sign):
    if (sign == "+"):
        return a+b
    elif (sign == "-"):
        return a-b
    elif (sign == "*"):
        return a*b
    elif (sign == "/"):
        return a/b