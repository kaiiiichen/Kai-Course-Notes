(lambda f: lambda x: f(f(x)))(lambda y: y * y)(3)
