def Y(f):
    """The Y ("paradoxical") combinator."""
    return f(lambda: Y(f)) # This is called "lazy evaluation" since if we write f(Y(f)) we'll encounter an infinite recursion.