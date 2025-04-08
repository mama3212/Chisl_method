import numpy as np


def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        # Верхняя треугольная матрица U
        for k in range(i, n):
            sum_ = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_

        # Нижняя треугольная матрица L
        for k in range(i, n):
            if i == k:
                L[i][i] = 1  # Диагональные элементы L равны 1
            else:
                sum_ = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (A[k][i] - sum_) / U[i][i]

    return L, U


def solve_lu(L, U, b):
    """
    Решает систему LUx = b.
    Сначала решает Ly = b (прямая подстановка),
    затем Ux = y (обратная подстановка).
    """
    n = len(b)

    # Решение Ly = b (прямая подстановка)
    y = np.zeros(n)
    for i in range(n):
        sum_ = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - sum_) / L[i][i]

    # Решение Ux = y (обратная подстановка)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum_ = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - sum_) / U[i][i]

    return x


def solve_system_with_lu(A, b):
    """
    Решает систему Ax = b с использованием LU-разложения.
    """
    # Выполняем LU-разложение
    L, U = lu_decomposition(A)

    # Решаем систему
    return solve_lu(L, U, b)


# Пример использования
if __name__ == "__main__":
    # Матрица коэффициентов
    A = np.array([
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2]
    ], dtype=float)

    # Вектор правых частей
    b = np.array([8, -11, -3], dtype=float)

    # Решение системы
    try:
        x = solve_system_with_lu(A, b)
        print("Решение системы:")
        print(x)

        # Проверка
        print("Проверка Ax - b:", np.dot(A, x) - b)

        # Вывод LU-разложения
        L, U = lu_decomposition(A)
        print("\nL-матрица:")
        print(L)
        print("\nU-матрица:")
        print(U)
    except Exception as e:
        print("Ошибка:", e)