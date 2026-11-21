import numpy as np
import matplotlib.pyplot as plt

x = [1, 2,  3,  4]
y = [1, 8, 27, 64]

def forward(x, y, x_n):
    arr = [y]
    for i in range(3):## it means at 3 times del y =0 and (n-1)th zero and for function nth time zero
        temp = []
        for j in range(0, len(arr[-1])-1):
            temp.append(arr[-1][j+1] - arr[-1][j])
        arr.append(temp)
    print("Forward difference table:", arr)

    h = (x_n - x[0]) / (x[1] - x[0])
    a = arr[0][0]
    b = h * arr[1][0]
    c = h * (h-1) / 2 * arr[2][0]
    d = h * (h-1) * (h-2) / 6 * arr[3][0]

    return a + b + c + d


def backward(x, y, x_n):
    arr = [y]
    for i in range(3):
        temp = []
        for j in range(0, len(arr[-1])-1):
            temp.append(arr[-1][j+1] - arr[-1][j])
        arr.append(temp)
    print("Backward difference table:", arr)

    h = (x_n - x[-1]) / (x[1] - x[0])
    a = arr[0][-1]                          # y_n
    b = h * arr[1][-1]                      # p * ∇y_n
    c = h * (h+1) / 2 * arr[2][-1]           # p(p+1)/2! * ∇²y_n
    d = h * (h+1) * (h+2) / 6 * arr[3][-1]   # p(p+1)(p+2)/3! * ∇³y_n

    return a + b + c + d


def lagrange(x, y, x_n):
    n = len(x)
    res = 0
    for i in range(n):
        temp = y[i]
        for j in range(n):
            if i != j:
                temp *= x_n - x[j]
                temp /= x[i] - x[j]
        res += temp
    return res

print("Forward:", forward(x, y, 2.5))
print("Backward:", backward(x, y, 3.5))
print("Lagrange:", lagrange(x, y, 2.5))