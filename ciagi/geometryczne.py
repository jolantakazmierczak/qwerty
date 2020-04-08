

def n_wyraz(n, a1, q):
    return a1 * q**(n-1)

def suma_n(n, a1, q):
    if (q==1):
        return n * a1
    else:
        return a1 * ((1 - q**n)/(1 - q))
1
