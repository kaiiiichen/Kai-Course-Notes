def plus1(n): return n + 1
def times3(n): return n * 3
def compose(f, g): return lambda n: f(g(n))
plus1times3 = compose(plus1, times3)
print(plus1times3(10))