def count_park(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return 2 * count_park(n - 1) + count_park(n - 2)
    
def park(n):
    if n < 0:
        return []
    elif n == 0:
        return ['']
    else:
        res_n1 = park(n - 1)
        res_n2 = park(n - 2)
        return [s + '.' for s in res_n1] + [s + '%' for s in res_n1] + [s + '<>' for s in res_n2]