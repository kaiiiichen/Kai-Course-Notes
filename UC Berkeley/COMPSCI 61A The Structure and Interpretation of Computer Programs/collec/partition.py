def list_partition(n, m):
    """Return all partitons of N with numbers not exceeding M using list comprehension.

    >>> for p in list_partition(6, 4): print(p)
    ... 
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [str(m)]
        with_m = [p + ' + ' + str(m) for p in list_partition(n-m, m)]
        without_m = list_partition(n, m-1)
        return exact_match + with_m + without_m
    

def partition(n, m):
    """Return all partitons of N with numbers not exceeding M using yield.

    >>> for p in partition(6, 4): print(p)
    ... 
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in partition(n-m, m):
            yield p + ' + ' + str(m)
        yield from partition(n, m-1)