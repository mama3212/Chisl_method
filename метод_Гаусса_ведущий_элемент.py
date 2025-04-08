import numpy as np


def gauss_with_pivoting(A, b):
    n = len(b)

    # Создаем расширенную матрицу [A|b]
    Ab = np.hstack([A.astype(float), b.reshape(-1, 1).astype(float)])

    # Прямой ход метода Гаусса
    for i in range(n):
        # Выбор ведущего элемента в текущем столбце
        max_row = np.argmax(np.abs(Ab[i:, i])) + i

        # Перестановка строк, если нужно
        if max_row != i:
            Ab[[i, max_row]] = Ab[[max_row, i]]

        # Проверка на вырожденность
        if np.abs(Ab[i, i]) < 1e-10:
            raise ValueError("Матрица системы вырождена или плохо обусловлена")

        # Нормализация текущей строки
        Ab[i] = Ab[i] / Ab[i, i]

        # Исключение переменной из нижележащих строк
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
    try:
        x = gauss_with_pivoting(A, b)
        print("Решение системы:")
        print(x)

        # Проверка
        print("Проверка Ax - b:", np.dot(A, x) - b)
    except ValueError as e:
        print("Ошибка:", e)