import numpy as np

# Определяем функцию и её производную
def f(x):
    return np.sin(x) + 0.5 * x - 1

def df(x):
    return np.cos(x) + 0.5

# Функция для отделения корней
def separate_roots(f, a, b, step=0.1):
    """
    Отделяет корни функции f на интервале [a, b] с шагом step.
    Возвращает список отрезков, на которых функция меняет знак.
    """
    segments = []
    x = a
    while x < b:
        if f(x) * f(x + step) < 0:
            segments.append((x, x + step))
        x += step
    return segments

# Метод половинного деления (бисекции)
def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    """
    Метод половинного деления для нахождения корня функции f на отрезке [a, b].
    tol - точность, max_iter - максимальное количество итераций.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("Функция должна иметь разные знаки на концах отрезка.")

    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iter_count += 1

    return (a + b) / 2

# Метод Ньютона
def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    """
    Метод Ньютона для нахождения корня функции f.
    df - производная функции, x0 - начальное приближение.
    """
    x = x0
    iter_count = 0
    while abs(f(x)) > tol and iter_count < max_iter:
        x = x - f(x) / df(x)
        iter_count += 1
    return x

# Основная программа
if __name__ == "__main__":
    # Отделяем корни на интервале [-10, 10]
    segments = separate_roots(f, -10, 10)
    print("Отрезки с корнями:", segments)

    if segments:
        # Находим корень методом бисекции на первом отрезке
        a, b = segments[0]
        root_bisection = bisection_method(f, a, b)
        print(f"Найденный корень методом бисекции на отрезке [{a}, {b}]:", root_bisection)

        # Уточняем корень методом Ньютона
        root_newton = newton_method(f, df, root_bisection)
        print("Уточненный корень методом Ньютона:", root_newton)
    else:
        print("Корни не найдены.")