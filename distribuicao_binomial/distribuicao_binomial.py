def fat(x):
    factorial = 1

    for i in range(1, x + 1):
        factorial *= i
    return factorial

def C(n, k):
    return fat(n)/(fat(k) * fat(n - k))

def P(p, n, k):
    q = 1 - p
    return C(n, k) * (p**k) * (q**(n-k))

if __name__ == "__main__":
    print(P(0.5, 5, 3))