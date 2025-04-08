import numpy as np


def gauss_elimination(A, b):
    """
    Решает систему линейных уравнений Ax = b методом Гаусса с выбором главного элемента.

    Параметры:
    A -- матрица коэффициентов (n x n)
    b -- вектор правых частей (n)

    Возвращает:
    x -- вектор решения
    """
    n = len(b)

    # Создаем расширенную матрицу
    Ab = np.hstack([A.astype(float), b.reshape(-1, 1).astype(float)])

    # Прямой ход метода Гаусса
    for i in range(n):
        # Выбор главного элемента (максимального по модулю в текущем столбце)
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        # Меняем строки местами, если нужно
        if max_row != i:
            Ab[[i, max_row]] = Ab[[max_row, i]]

        # Нормализация текущей строки
        Ab[i] = Ab[i] / Ab[i, i]

        # Исключение переменной из остальных уравнений
        for k in range(i + 1, n):
            Ab[k] = Ab[k] - Ab[k, i] * Ab[i]

    # Обратный ход метода Гаусса
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:])

    return x


# Пример использования
if __name__ == "__main__":
    # Матрица коэффициентов
    A = np.array([
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2]
    ])

    # Вектор правых частей
    b = np.array([8, -11, -3])

    # Решение системы
    x = gauss_elimination(A, b)
    print("Решение системы:")
    print(x)

    # Проверка
    print("Проверка Ax - b:", np.dot(A, x) - b)