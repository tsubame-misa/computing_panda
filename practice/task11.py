# 最急降下法

A = [[2, -1, 0], [-1, 3, -1], [0, -1, 3]]
b = [100, 50, 50]


def calc_delta(x, weight=1):
    delta = []
    for i in range(3):
        p = 0
        for j in range(3):
            p += A[i][j]*x[j]
        delta.append((p-b[i])*weight)
    return delta


def calc_a(x, d):
    delta = calc_delta(x)
    print(delta)

    delta_d = 0
    for i in range(3):
        delta_d += delta[i]*d[i]
    dad = 0
    for i in range(3):
        for j in range(3):
            dad += d[i]*d[j]*A[i][j]
    return -1*(delta_d/dad)


def calc_delta_norm(x):
    delta = calc_delta(x)
    return sum([x**2 for x in delta])**0.5


eps = 1e-6
k = 0
x_k = [0, 1, 2]
while not calc_delta_norm(x_k) <= eps:
    print("norm", calc_delta_norm(x_k))
    d_k = calc_delta(x_k, -1)
    print("d_k", d_k)
    a = calc_a(x_k, d_k)
    print("a", a)
    x_k1 = [x_k[i]+a*d_k[i] for i in range(3)]
    print("x", x_k1)
    x_k = x_k1
    k += 1
    print()

print("fin -------------------")
print("norm", calc_delta_norm(x_k))
print("d", d_k)
print("x", x_k)
print("k", k)
