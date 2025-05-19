import numpy as np

def jacobi_rotation_method(A, tol=1e-10, max_iterations=100):
    n = A.shape[0]
    if not np.allclose(A, A.T, atol=1e-10):
        raise ValueError("Matrix must be symmetric.")

    A = A.copy()
    V = np.eye(n)

    for _ in range(max_iterations):
        max_val = 0
        p, q = 0, 1
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i, j]) > abs(max_val):
                    max_val = A[i, j]
                    p, q = i, j

        if abs(max_val) < tol:
            break

        if A[p, p] == A[q, q]:
            theta = np.pi / 4
        else:
            tau = (A[q, q] - A[p, p]) / (2 * A[p, q])
            t = np.sign(tau) / (abs(tau) + np.sqrt(1 + tau ** 2))
            theta = np.arctan(t)

        c = np.cos(theta)
        s = np.sin(theta)

        for i in range(n):
            if i != p and i != q:
                aip = A[i, p]
                aiq = A[i, q]
                A[i, p] = A[p, i] = c * aip - s * aiq
                A[i, q] = A[q, i] = s * aip + c * aiq

        app = A[p, p]
        aqq = A[q, q]
        apq = A[p, q]

        A[p, p] = c**2 * app - 2 * s * c * apq + s**2 * aqq
        A[q, q] = s**2 * app + 2 * s * c * apq + c**2 * aqq
        A[p, q] = A[q, p] = 0.0

        for i in range(n):
            vip = V[i, p]
            viq = V[i, q]
            V[i, p] = c * vip - s * viq
            V[i, q] = s * vip + c * viq

    eigenvalues = np.diag(A)
    return eigenvalues, V



A = np.array([
    [4.0, 1.0, 1.0],
    [1.0, 3.0, 0.0],
    [1.0, 0.0, 2.0]
])

eigvals, eigvecs = jacobi_rotation_method(A)

print("Собственные значения:")
print(eigvals)

print("\nСобственные векторы (по столбцам):")
print(eigvecs)
