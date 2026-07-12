def fact(n):
    return fact_times(n, 1)

def fact_times(n, k):
    """Return k * n!"""
    if n == 0:
        return k
    else:
        return fact_times(n - 1, k * n)