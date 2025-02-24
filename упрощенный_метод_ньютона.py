def simplified_newton_method(f, df_x0, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        fx = f(x)

        if abs(fx) < tol:
            return x

        if df_x0 == 0:
            print("Ошибка: производная равна нулю, метод не применим.")
            return None

        x = x - fx / df_x0

    print("Достигнуто максимальное число итераций.")
    return x


def func(x):
    return x ** 2 - 2


df_x0 = 2 * 1.5

root = simplified_newton_method(func, df_x0, x0=1.5)
print(f"Найденный корень: {root}")
