import numpy as np


def broyden_method(F, x0, B0, tol=1e-6, max_iter=100):
    x = x0
    B = B0
    Fx = F(x)

    for i in range(max_iter):
        if np.linalg.norm(Fx) < tol:
            print(f"Решение найдено за {i} итераций.")
            return x

        dx = -np.linalg.solve(B, Fx)
        x_new = x + dx
        Fx_new = F(x_new)

        y = Fx_new - Fx
        B = B + np.outer((y - B @ dx), dx) / np.dot(dx, dx)

        x = x_new
        Fx = Fx_new

    print("Достигнуто максимальное количество итераций.")
    return x


# Пример использования:
def system_of_equations(x):
    return np.array([
        x[0] + x[1] - 3,
        x[0] ** 2 + x[1] ** 2 - 9
    ])


x0 = np.array([1.0, 2.0])

B0 = np.eye(2)

solution = broyden_method(system_of_equations, x0, B0)

print("Решение:", solution)