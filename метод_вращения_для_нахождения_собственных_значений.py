import numpy as np

def jacobi_rotation_2x2(A):
    if not np.allclose(A, A.T):
        raise ValueError("Matrix must be symmetric")

    a, b = A[0, 0], A[0, 1]
    d = A[1, 1]

    if np.isclose(b, 0):
        eigenvalues = [a, d]
        eigenvectors = np.eye(2)
    else:
        tau = (d - a) / (2 * b)
        t = np.sign(tau) / (abs(tau) + np.sqrt(1 + tau**2))
        c = 1 / np.sqrt(1 + t**2)
        s = t * c

        R = np.array([[c, -s], [s, c]])

        D = R.T @ A @ R
        eigenvalues = np.diag(D)
        eigenvectors = R

    return eigenvalues, eigenvectors


A = np.array([[4, 1],
              [1, 3]])

eigvals, eigvecs = jacobi_rotation_2x2(A)

print("Собственные значения:", eigvals)
print("Собственные векторы:\n", eigvecs)
