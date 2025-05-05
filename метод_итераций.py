import numpy as np


def power_iteration(A, num_iter=1000, eps=1e-10):
    n = A.shape[0]
    b_k = np.random.rand(n)

    for _ in range(num_iter):
        b_k1 = np.dot(A, b_k)
        eigenvalue = np.linalg.norm(b_k1)
        b_k1 = b_k1 / eigenvalue

        if np.linalg.norm(b_k1 - b_k) < eps:
            break

        b_k = b_k1

    eigenvalue = np.dot(b_k, np.dot(A, b_k)) / np.dot(b_k, b_k)
    return eigenvalue, b_k


A = np.array([[4, -1, 1],
              [-1, 3, -2],
              [1, -2, 3]])

val, vec = power_iteration(A)
print(val)
print(vec)