import numpy as np


def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if abs(fx) < tol:
            return x

        if dfx == 0:
            raise ValueError("Производная равна нулю, метод Ньютона не работает.")

        x -= fx / dfx

    raise ValueError("Превышено максимальное число итераций")


def func(x):
    return x ** 3 - 2 * x - 5


def dfunc(x):
    return 3 * x ** 2 - 2

#пример
x0 = 2
root = newton_method(func, dfunc, x0)
print("Найденный корень:", root)
