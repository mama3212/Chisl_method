def chord_method(func, a, b, tol=1e-6, max_iter=100):
    """
    Реализация метода хорд для нахождения корня функции.

    :param func: Функция, корень которой мы ищем.
    :param a: Начальная точка интервала.
    :param b: Конечная точка интервала.
    :param tol: Точность (критерий остановки).
    :param max_iter: Максимальное количество итераций.
    :return: Приближенное значение корня.
    """
    if func(a) * func(b) >= 0:
        raise ValueError("Функция должна иметь разные знаки на концах интервала [a, b].")

    iter_count = 0
    while iter_count < max_iter:
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))

        # Проверяем, достигли ли мы нужной точности
        if abs(func(c)) < tol:
            return c

        # Обновляем интервал
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

        iter_count += 1

    raise ValueError(f"Метод не сошелся за {max_iter} итераций.")

def f(x):
    return x**3 - 2*x - 5

root = chord_method(f, 1, 3)
print(f"Найденный корень: {root}")

