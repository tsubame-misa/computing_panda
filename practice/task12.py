# ニュートン方
import numpy as np

A = np.array([[2, -1, 0], [-1, 3, -1], [0, -1, 3]])
b = np.array([[100], [50], [50]])


# wは重み
def get_delta(x, w=1):
    return (np.dot(A, x) - b)*w


def get_delta_nrm(x):
    delta = get_delta(x)
    # ord=2が各次元の値を2乗した和の平方根
    return np.linalg.norm(delta, ord=2)


def calc_d(x):
    delta = get_delta(x)
    return -1*(np.dot(np.linalg.inv(A), delta))


eps = 1e-6
k = 0
x_k = np.array([[0], [1], [2]])

while not get_delta_nrm(x_k) <= eps:
    d_k = calc_d(x_k)
    x_k = x_k + d_k
    k += 1

print("fin -------------------")
print("norm", get_delta_nrm(x_k))
print("d", d_k)
print("x", x_k)
print("k", k)
