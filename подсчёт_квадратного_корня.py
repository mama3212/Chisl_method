def sqrt_iterative(a, x0, tol=1e-6, max_iter=100):
    if a < 0:
        raise ValueError("Число 'a' должно быть неотрицательным.")
    if x0 <= 0:
        raise ValueError("Начальное приближение 'x0' должно быть положительным.")

    x = x0
    for i in range(max_iter):
        x_next = 0.5 * (x + a / x)

        if abs(x_next - x) < tol:
            print(f"Квадратный корень найден за {i} итераций.")
            return x_next

        x = x_next

    print("Достигнуто максимальное количество итераций.")
    return x


a = 2
x0 = 1

sqrt_value = sqrt_iterative(a, x0)

print("Приближённое значение квадратного корня:", sqrt_value)