def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if abs(f_x1) < tol:
            print(f"Корень найден за {i} итераций.")
            return x1

        x_next = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        x0, x1 = x1, x_next

    print("Достигнуто максимальное количество итераций.")
    return x1


def f(x):
    return x ** 3 - 2 * x - 5

x0 = 2.0
x1 = 3.0

root = secant_method(f, x0, x1)

print("Найденный корень:", root)