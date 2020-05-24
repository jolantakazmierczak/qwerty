import numpy as np
def fun(n):
    a = [1, 1]
    for i in range(n*n-2):
        a.append(a[i] + a[(i + 1)])
    fi = np.asarray(a)
    b = np.reshape(fi, (n, n))
    print(b)


fun(5)