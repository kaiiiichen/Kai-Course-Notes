def gcd(n, d):
    while n != d:
        n, d = min(n, d), abs(n-d)
    return n