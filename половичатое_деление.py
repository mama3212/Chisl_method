def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Значения функции на концах интервала должны иметь разные знаки")

    for i in range(max_iter):
        c = (a + b) / 2.0
        fc = f(c)

        if abs(fc) < tol or (b - a) / 2 < tol:
            return c

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    raise ValueError("Превышено максимальное число итераций")


# Пример использования:
def func(x):
    return x ** 3 - 2 * x - 5


root = bisection_method(func, 2, 3)
print("Найденный корень:", root)
