import numpy as np


def power_method(A, eps=1e-6, max_iter=1000):
    n = A.shape[0]
    v = np.random.rand(n)
    v = v / np.linalg.norm(v)
    lambda_prev = 0

    for _ in range(max_iter):
        Av = A @ v
        v_new = Av / np.linalg.norm(Av)
        lambda_new = (v_new.T @ A @ v_new) / (v_new.T @ v_new)

        if np.abs(lambda_new - lambda_prev) < eps:
            break

        v = v_new
        lambda_prev = lambda_new

    return lambda_new, v_new

A = np.array([[2, -1, 0],
              [-1, 2, -1],
              [0, -1, 2]])

lambda1, v1 = power_method(A)
print("Наибольшее собственное значение:", lambda1)
print("Соответствующий собственный вектор:", v1)