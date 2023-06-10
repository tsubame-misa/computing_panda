# 共役勾配法
import numpy as np

A = np.array([[2, -1, 0], [-1, 3, -1], [0, -1, 3]])
b = np.array([[100], [50], [50]])


def get_delta(x):
    return A@x - b


def calc_a(x, d):
    delta = get_delta(x)
    delta_d = delta.T@d
    dad = (d.T@A)@d
    return -1*(delta_d/dad)


def get_delta_nrm(x):
    delta = get_delta(x)
    # ord=2が各次元の値を2乗した和の平方根
    return np.linalg.norm(delta, ord=2)


k = 0
x_k = np.array([[0], [1], [2]])
d_k = -1*get_delta(x_k)
for k in range(len(x_k)):
    a = calc_a(x_k, d_k)
    x_k1 = x_k + a*d_k
    beta = get_delta_nrm(x_k1)**2/(get_delta_nrm(x_k)**2)
    d_k = -1*get_delta(x_k1)+beta*d_k
    x_k = x_k1

print(x_k)
