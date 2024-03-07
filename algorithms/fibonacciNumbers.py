def fibonacciRecursive(n):
    if n<2: return n
    else:
        return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)