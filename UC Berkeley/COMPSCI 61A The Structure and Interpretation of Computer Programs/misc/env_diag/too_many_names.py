def f(x):
    f = 10
    z = 100
    x = g(x)(f)
    def f(x):
        return x + y
    return f
    
def g(g):
    return lambda g: g + z

z = 3
f = f(5)