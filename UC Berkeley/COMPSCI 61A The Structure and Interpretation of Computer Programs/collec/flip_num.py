"flip the number KEEP an return as N"

def flip(keep):
    n = 0
    while keep > 0:
        n, keep = 10 * n + keep % 10, keep // 10
    return n