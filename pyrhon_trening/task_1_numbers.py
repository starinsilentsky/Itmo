def task_1() -> None:
    # Создание переменных разных типов
    int_var: int = 10
    float_var: float = 3.14
    str_var: str = "classic"
    list_var: list = [1, 2, 3]
    bool_var: bool = True

    # Вывод типа данных каждой переменной
    print(type(int_var))
    print(type(float_var))
    print(type(str_var))
    print(type(list_var))
    print(type(bool_var))


task_1()  # Вызов функции


def task_2() -> None:
    # Последовательность чисел
    a = [1, 2, 3, 5, 8, 13, 21]

    # Вывод первых трех значений списка
    print(a[:3])


task_2()  # Вызов функции




def task_3(num: int) -> int:
    return num ** 2  #возведение в квадрат числа и его возвращение


print(task_3(5))  # Вывод результата вызова функции